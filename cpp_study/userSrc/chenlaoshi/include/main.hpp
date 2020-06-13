#pragma once
#include "lv_drivers/display/monitor.h"
#include "lv_drivers/indev/keyboard.h"
#include "lv_drivers/indev/mouse.h"
#include "lv_examples/lv_apps/benchmark/benchmark.h"
#include "lv_examples/lv_apps/demo/demo.h"
#include "lv_examples/lv_tests/lv_test_theme/lv_test_theme_1.h"
#include "lv_examples/lv_tutorial/10_keyboard/lv_tutorial_keyboard.h"
#include "lvgl/lvgl.h"
#include "userAPI.hpp"
#include <SDL2/SDL.h>
#include <Windows.h>
#include <stdlib.h>
static void hal_init(void);
static int tick_thread(void *data);

/**********************
 *  STATIC VARIABLES
 **********************/
static lv_indev_t *kb_indev;