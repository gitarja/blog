#include "FaceTracking.h"


#define ERROR_CHECK(ret) if(ret != S_OK){std::stringstream ss; ss << "failed" #ret " " << std::hex << ret << std::endl; throw std::runtime_error(ss.str().c_str() );}




FaceTracking::FaceTracking(void)
{

}


FaceTracking::~FaceTracking(void)
{
}

void FaceTracking::initializeHDFace(IKinectSensor* kinect) {

	//start body tracking
	ERROR_CHECK(kinect->get_BodyFrameSource(&bodyFrameSource));
	ERROR_CHECK(bodyFrameSource->OpenReader(&bodyFrameReader));
	//end body tracking

	//start color frame

	CComPtr<IColorFrameSource> colorFrameSource;
	ERROR_CHECK(kinect->get_ColorFrameSource(&colorFrameSource));
	ERROR_CHECK(colorFrameSource->OpenReader(&colorFrameReader));
	CComPtr<IFrameDescription> colorFrameDescription;
	ERROR_CHECK(colorFrameSource->CreateFrameDescription(ColorImageFormat::ColorImageFormat_Bgra, &colorFrameDescription));
	ERROR_CHECK(colorFrameDescription->get_Width(&colorWidth));
	ERROR_CHECK(colorFrameDescription->get_Height(&colorHeight));
	ERROR_CHECK(colorFrameDescription->get_BytesPerPixel(&colorBytesPixel));
	colorBuffer.resize(colorWidth * colorHeight * colorBytesPixel);
	ERROR_CHECK(kinect->get_CoordinateMapper(&coordinateMapper));
	//end color frame

	//start intialize hdFace Tracking
	CComPtr<IHighDefinitionFaceFrameSource> hdfaceFrameSource;
	ERROR_CHECK(CreateHighDefinitionFaceFrameSource(kinect, &hdfaceFrameSource));
	ERROR_CHECK(hdfaceFrameSource->OpenReader(&hdFaceFrameReader));
	ERROR_CHECK(CreateFaceAlignment(&faceAligment));

	ERROR_CHECK(CreateFaceModel(1.0f, FaceShapeDeformations::FaceShapeDeformations_Count, &shapeUnits[0], &faceModel));
	ERROR_CHECK(GetFaceModelVertexCount(&vertexCount));

	FaceModelBuilderAttributes attribures = FaceModelBuilderAttributes::FaceModelBuilderAttributes_None;
	ERROR_CHECK(hdfaceFrameSource->OpenModelBuilder(attribures, &faceModelBuilder));
	ERROR_CHECK(faceModelBuilder->BeginFaceDataCollection());
	//end intialize hdFace Tracking


}

void FaceTracking::updateBodyFrame() {
	CComPtr<IBodyFrame> bodyFrame;
	HRESULT ret = bodyFrameReader->AcquireLatestFrame(&bodyFrame);
	if (FAILED(ret))
	{
		return;
	}

	std::array<CComPtr<IBody>, BODY_COUNT> bodies;

	ERROR_CHECK(bodyFrame->GetAndRefreshBodyData(BODY_COUNT, &bodies[0]));
	findClosestBody(bodies);


}

void FaceTracking::findClosestBody(const std::array<CComPtr<IBody>, BODY_COUNT> &bodies) {
	float closest = FLT_MAX;
	for (int count = 0; count < BODY_COUNT; count++) {
		CComPtr<IBody> body = bodies[count];
		BOOLEAN tracked;
		ERROR_CHECK(body->get_IsTracked(&tracked));
		//std::cout << std::noboolalpha << tracked << " == " << std::boolalpha << tracked << std::endl;
		if (!tracked) {
			continue;
		}

		std::array < Joint, JointType::JointType_Count> joints;
		ERROR_CHECK(body->GetJoints(JointType::JointType_Count, &joints[0]));
		Joint position = joints[JointType::JointType_Head];

		if (position.TrackingState == TrackingState::TrackingState_NotTracked) {
			continue;
		}

		CameraSpacePoint point = position.Position;
		float distance = std::sqrt(std::pow(point.X, 2) + std::pow(point.Y, 2) + std::pow(point.Z, 2));
		if (closest <= distance) {
			continue;
		}
		closest = distance;

		UINT64 id;
		ERROR_CHECK(body->get_TrackingId(&id));
		//std::cout << id;
		if (trackingId != id) {
			trackingId = id;
			trackingCount = count;
			produced = false;

			CComPtr<IHighDefinitionFaceFrameSource> hdFaceFrameSource;
			ERROR_CHECK(hdFaceFrameReader->get_HighDefinitionFaceFrameSource(&hdFaceFrameSource));
			ERROR_CHECK(hdFaceFrameSource->put_TrackingId(trackingId));
		}
	}
}

void FaceTracking::updateHDFaceFrame() {
	updateColorFrame();
	CComPtr<IHighDefinitionFaceFrame> hdFaceFrame;
	HRESULT ret = hdFaceFrameReader->AcquireLatestFrame(&hdFaceFrame);
	//set eyes to null
	leftEye.release();
	rightEye.release();
	if (FAILED(ret)) {
		return;
	}

	BOOLEAN tracked;
	ERROR_CHECK(hdFaceFrame->get_IsFaceTracked(&tracked));

	if (!tracked) {
		return;
	}

	ERROR_CHECK(hdFaceFrame->GetAndRefreshFaceAlignmentResult(faceAligment));
	

	if (faceAligment != nullptr) {
		ERROR_CHECK(faceAligment->get_FaceOrientation(&headOrientation));
		buildfaceModel();

		result();
	}


	//std::cout << "There is face";


}
void FaceTracking::updateColorFrame() {
	CComPtr<IColorFrame> colorFrame;
	auto ret = colorFrameReader->AcquireLatestFrame(&colorFrame);
	if (FAILED(ret)) {
		return;
	}

	ERROR_CHECK(colorFrame->CopyConvertedFrameDataToArray(colorBuffer.size(), &colorBuffer[0], colorFormat));
	colorImage = cv::Mat(colorHeight, colorWidth, CV_8UC4, &colorBuffer[0]);
	//proceedColorImage = cv::Mat(colorHeight, colorWidth, CV_8UC4, &colorBuffer[0]);
	colorImage.copyTo(proceedColorImage);
	//cv::imshow("Test", colorImage);


}
inline void FaceTracking::buildfaceModel() {
	int font = FONT_HERSHEY_SCRIPT_SIMPLEX;

	if (produced) {
		cv::putText(colorImage, "Status: Complete", cv::Point(50, 50), font, 1.0f, colors, 2, CV_AA);
	}

	FaceModelBuilderCollectionStatus collection;
	ERROR_CHECK(faceModelBuilder->get_CollectionStatus(&collection));
	if (collection) {
		std::string status = status2string(collection);
		cv::putText(colorImage, "Status : " + status, cv::Point(50, 50), font, 1.0f, colors, 2, CV_AA);


		FaceModelBuilderCaptureStatus capture;
		ERROR_CHECK(faceModelBuilder->get_CaptureStatus(&capture));
		status = status2string(capture);
		cv::putText(colorImage, status, cv::Point(50, 11), font, 1.0f, colors, 2, CV_AA);
	}
}
std::string FaceTracking::status2string(const FaceModelBuilderCollectionStatus collection) {
	std::string status;

	if (collection & FaceModelBuilderCollectionStatus::FaceModelBuilderCollectionStatus_LeftViewsNeeded) {
		status = "Need : Tilted Up Views";
	}
	else if (collection & FaceModelBuilderCollectionStatus::FaceModelBuilderCollectionStatus_RightViewsNeeded) {
		status = "Need : Right Views";
	}
	else if (collection & FaceModelBuilderCollectionStatus::FaceModelBuilderCollectionStatus_LeftViewsNeeded) {
		status = "Need : Left Views";
	}
	else if (collection & FaceModelBuilderCollectionStatus::FaceModelBuilderCollectionStatus_FrontViewFramesNeeded) {
		status = "Need : Front ViewFrames";
	}
	return status;
}

inline std::string FaceTracking::status2string(const FaceModelBuilderCaptureStatus capture) {
	std::string status;

	switch (capture)
	{
	case FaceModelBuilderCaptureStatus::FaceModelBuilderCaptureStatus_FaceTooFar:
		status = "Error: Face Too Far from Camera";
	case FaceModelBuilderCaptureStatus::FaceModelBuilderCaptureStatus_FaceTooNear:
		status = "Error: Face Too Near from Camera";
	case FaceModelBuilderCaptureStatus::FaceModelBuilderCaptureStatus_MovingTooFast:
		status = "Error: Moving Too Fast";
	default:
		status = "";
		break;
	}
	return status;
}

void FaceTracking::result() {
	std::vector<CameraSpacePoint> vertexs(vertexCount);
	ERROR_CHECK(faceModel->CalculateVerticesForAlignment(faceAligment, vertexCount, &vertexs[0]));

	int coor[8] = { HighDetailFacePoints_LefteyeInnercorner, HighDetailFacePoints_LefteyeOutercorner, HighDetailFacePoints_LefteyeMidtop, HighDetailFacePoints_LefteyeMidbottom,
		HighDetailFacePoints_RighteyeInnercorner , HighDetailFacePoints_RighteyeOutercorner , HighDetailFacePoints_RighteyeMidtop , HighDetailFacePoints_RighteyeMidbottom };
	Scalar colorList[4] = { cv::Scalar(255),  cv::Scalar(0, 0, 255), cv::Scalar(0, 255, 0),  cv::Scalar(255, 255, 255) };
	int xEye[8];
	int yEye[8];
	cv::Point2f inputQuad[4];
	

	for (const CameraSpacePoint v : vertexs) {
		ColorSpacePoint point;
		ERROR_CHECK(coordinateMapper->MapCameraPointToColorSpace(v, &point));
		int x = static_cast<int>(std::ceil(point.X));
		int y = static_cast<int> (std::ceil(point.Y));


		if ((x >= 0) && (x < colorWidth) && (y >= 0) && (y < colorHeight)) {
			cv::circle(colorImage, cv::Point(x, y), 2, colors, -1, CV_AA);
			
		}

	}



}

cv::Mat FaceTracking::getImage() {
	return FaceTracking::colorImage;
}

cv::Mat FaceTracking::getLeftEye() {
	return FaceTracking::leftEye;
}

cv::Mat FaceTracking::getRightEye() {
	return FaceTracking::rightEye;
}
std::vector<double> FaceTracking::getHeadOrientation() {
	std::vector<double> headOrientation(3);
	//pitch
	headOrientation.at(0) = FaceTracking::headOrientation.x;
	//yaw
	headOrientation.at(1) = FaceTracking::headOrientation.y;
	//roll
	headOrientation.at(2) = FaceTracking::headOrientation.z;
	return headOrientation;
}
