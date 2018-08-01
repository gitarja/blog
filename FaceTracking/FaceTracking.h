#pragma once
#include <array>
#include <vector>
#include <iostream>
#include <sstream>
#include <atlbase.h>
#include <Kinect.h>
#include <Kinect.Face.h>
#include "opencv2\opencv.hpp"
#include "Feature.h"
#include "Eyes.h"
#define w 70
#define h 40
using namespace std;
using namespace cv;
class FaceTracking
{
public:
	FaceTracking(void);
	~FaceTracking(void);

public:
	void initializeHDFace(IKinectSensor* kinect);
	void updateHDFaceFrame();
	void updateBodyFrame();
	cv::Mat getImage();
	//eye result
	cv::Mat getLeftEye();
	cv::Mat getRightEye();
	//head orientation
	std::vector<double> getHeadOrientation();

private:

	IKinectSensor* kinect;
	//body tracking
	CComPtr<IBodyFrameSource> bodyFrameSource;
	CComPtr<IBodyFrameReader> bodyFrameReader;
	//hdFaceTracking
	CComPtr<IHighDefinitionFaceFrameReader> hdFaceFrameReader = nullptr;
	CComPtr<IFaceModelBuilder> faceModelBuilder;
	CComPtr<IFaceAlignment> faceAligment;
	CComPtr<IFaceModel> faceModel;
	array<float, FaceShapeDeformations::FaceShapeDeformations_Count> shapeUnits;
	UINT32 vertexCount;
	UINT64 trackingId;
	int trackingCount;
	bool produced;
	//color frame
	CComPtr<IColorFrameReader> colorFrameReader = nullptr;
	CComPtr<ICoordinateMapper> coordinateMapper;
	int colorWidth;
	int colorHeight;
	unsigned int colorBytesPixel;
	cv::Mat colorImage;
	cv::Mat proceedColorImage;
	ColorImageFormat colorFormat = ColorImageFormat::ColorImageFormat_Bgra;
	std::vector<BYTE> colorBuffer;
	//function facehdTracking
	void result();
	void findClosestBody(const std::array<CComPtr<IBody>, BODY_COUNT> &bodies);
	inline void buildfaceModel();
	inline std::string status2string(const FaceModelBuilderCollectionStatus capture);
	inline std::string status2string(const FaceModelBuilderCaptureStatus capture);
	Scalar colors = cv::Scalar(255);

	//function color
	void updateColorFrame();

	//eyeResult
	cv::Point2f outputQuad[4] = { cv::Point2f(0, 0), cv::Point2f(w, 0), cv::Point2f(0, h), cv::Point2f(w, h) };
	cv::Mat leftEye;
	cv::Mat rightEye;

	//head position
	Vector4 headOrientation;





};

