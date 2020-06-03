#pragma once
#include <QPushButton>
class sonWidget :public QWidget
{
	Q_OBJECT
public:
	explicit sonWidget(QWidget *parent = Q_NULLPTR);
	~sonWidget(){}
	void sendSlot();
signals:
	void sonSignal();//×¢ÒâÐ´·¨ 
	//void sonSignal(int,QString);
private:
	QPushButton _btn_change;
};

