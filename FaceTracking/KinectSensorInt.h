#pragma once
#include <Kinect.h>
#include <sstream>
#include "opencv2\opencv.hpp"
#include <atlbase.h>
using namespace cv;
using namespace std;
class KinectSensorInt
{
public:
	KinectSensorInt(IKinectSensor* &kinect);
	~KinectSensorInt(void);

public:
	void getDepthFrame(cv::Mat &bufferMat);


private:
	//IKinectSensor* kinect;
	IDepthFrameSource* pDepthSource;
	IDepthFrameReader* pDepthReader;



};

