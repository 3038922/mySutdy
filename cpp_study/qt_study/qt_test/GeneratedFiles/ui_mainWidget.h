/********************************************************************************
** Form generated from reading UI file 'mainWidget.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWIDGET_H
#define UI_MAINWIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_mainWidgetClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *mainWidgetClass)
    {
        if (mainWidgetClass->objectName().isEmpty())
            mainWidgetClass->setObjectName(QStringLiteral("mainWidgetClass"));
        mainWidgetClass->resize(600, 400);
        menuBar = new QMenuBar(mainWidgetClass);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        mainWidgetClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(mainWidgetClass);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        mainWidgetClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(mainWidgetClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        mainWidgetClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(mainWidgetClass);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        mainWidgetClass->setStatusBar(statusBar);

        retranslateUi(mainWidgetClass);

        QMetaObject::connectSlotsByName(mainWidgetClass);
    } // setupUi

    void retranslateUi(QMainWindow *mainWidgetClass)
    {
        mainWidgetClass->setWindowTitle(QApplication::translate("mainWidgetClass", "mainWidget", nullptr));
    } // retranslateUi

};

namespace Ui {
    class mainWidgetClass: public Ui_mainWidgetClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWIDGET_H
