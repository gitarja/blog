
#include "KinectSensorInt.h"


#define ERROR_CHECK(ret) if(ret != S_OK){std::stringstream ss; ss << "failed" #ret " " << std::hex << ret << std::endl; throw std::runtime_error(ss.str().c_str() );}
template<class Interface>
inline void SafeRelease(Interface *& pInterfaceToRelease)
{
	if (pInterfaceToRelease != NULL)
	{
		pInterfaceToRelease->Release();
		pInterfaceToRelease = NULL;
	}
}


KinectSensorInt::KinectSensorInt(IKinectSensor* &kinect)
{
	ERROR_CHECK(::GetDefaultKinectSensor(&kinect));
	ERROR_CHECK(kinect->Open());
	//ERROR_CHECK(kinect->get_DepthFrameSource(&pDepthSource));
	//ERROR_CHECK(pDepthSource->OpenReader(&pDepthReader));
}
KinectSensorInt::~KinectSensorInt(void)
{
}

void KinectSensorInt::getDepthFrame(cv::Mat &bufferMat) {
	cv::Size s = bufferMat.size();
	unsigned int bufferSize = s.width * s.height * sizeof(unsigned short);
	cv::Mat bufferMatx(s.height, s.width, CV_16UC1);
	cv::Mat depthMat(s.height, s.width, CV_8UC1);
	IDepthFrame* pDepthFrame = nullptr;
	auto ret = pDepthReader->AcquireLatestFrame(&pDepthFrame);
	if (FAILED(ret)) {
		return;
	}
	ERROR_CHECK(pDepthFrame->AccessUnderlyingBuffer(&bufferSize, reinterpret_cast<UINT16**>(&bufferMatx.data)));
	bufferMatx.convertTo(bufferMat, CV_8U, -255.0f / 8000.0f, 255.0f);
	SafeRelease(pDepthFrame);


}





