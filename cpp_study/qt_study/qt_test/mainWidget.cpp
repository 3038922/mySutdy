#include "mainWidget.h"
#include <QDebug>
mainWidget::mainWidget(QWidget *parent)	:QWidget(parent)
{
	//ui.setupUi(this);
	setWindowTitle("i am father");
	resize(800, 600);
	_btn_change.setParent(this);
	_btn_change.resize(100,50);
	_btn_change.move(100, 100);
	_btn_change.setText("changToSon");

	_btn_close.setParent(this);
	_btn_close.resize(100, 50);
	_btn_close.move(300, 100);
	_btn_close.setText("close");
	son.setWindowTitle("i am son");
	son.resize(800, 600);
	connect(&_btn_close,&QPushButton::pressed,this,&mainWidget::close);//�ǵö��Ǵ���ַ
	connect(&_btn_change, &QPushButton::pressed, this, &mainWidget::_btn_change_slot);//�Զ���� �л����Ӵ���
	connect(&_btn_change, &QPushButton::pressed, []() { qDebug() << "���ɵȱ" << endl; });
	connect(&son, &sonWidget::sonSignal,this,&mainWidget::_btn_change_slot2);//���յ����ӵ��źŵ�ʱ��,��������һ����
	
}
