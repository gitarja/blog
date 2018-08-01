#include "VisualAttetion.h"
#include <QtWidgets/QApplication>
#include <QDebug>
#include <boost\regex.hpp>

int main(int argc, char *argv[])
{
  

	std::string line;
	boost::regex pat("^Subject: (Re: |Aw: )*(.*)");

	while (std::cin)
	{
		std::getline(std::cin, line);
		boost::smatch matches;
		if (boost::regex_match(line, matches, pat))
			std::cout << matches[2] << std::endl;
	}


	QApplication a(argc, argv);
	VisualAttetion w;
	//w.setUp();
	
	w.show();
	return a.exec();
}
