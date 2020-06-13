#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_mainWidget.h"
#include <QPushButton>
#include "sonWidget.h"
class mainWidget : public QWidget
{
	Q_OBJECT

public:
	mainWidget(QWidget *parent = Q_NULLPTR);

private:
	//Ui::mainWidgetClass ui;
	QPushButton _btn_change;
	QPushButton _btn_close;
	sonWidget son;
	void _btn_change_slot()
	{
		this->hide();
		son.show();
	}
	void _btn_change_slot2()
	{
		this->show();
		son.hide();
	}
};
