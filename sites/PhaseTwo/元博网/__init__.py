#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chinabidding.cn/public/2020/html/login.html?source=1")
    page.get_by_placeholder("请输入用户名/手机号").click()
    page.get_by_placeholder("请输入用户名/手机号").fill("ckyb414")
    page.get_by_placeholder("请输入登录密码").click()
    page.get_by_placeholder("请输入登录密码").fill("cky610072")
    page.locator("#loginimage-l").click()
    time.sleep(1)
    # page.get_by_text("快速登录").click()
    storage = context.storage_state(path="auth/state.json")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

