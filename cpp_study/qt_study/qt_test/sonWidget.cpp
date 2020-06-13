#include"sonWidget.h"
sonWidget::sonWidget(QWidget *parent):QWidget(parent)
{

	_btn_change.setParent(this);
	_btn_change.resize(100, 50);
	_btn_change.move(100, 100);
	_btn_change.setText("changToFather");
	sonWidget::connect(&_btn_change, &QPushButton::pressed, this, &sonWidget::sendSlot);
}
void sonWidget::sendSlot()
{
	emit sonSignal();
	//emit sonSignal(250, "i am son");
}