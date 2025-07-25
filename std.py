#!/bin/env python3
# -*- coding: UTF-8 -*-
from os import startfile
from subprocess import run
from manim import *


def render(py_file_path: str, classname: str | None = None, merge_audio: bool = False):
    filename = py_file_path.split("\\")[-1].split(".")[0]
    dir_name = py_file_path.split("\\")[-2]
    if classname == None:
        classname = filename

    if merge_audio:
        run(f"manim --save_sections {py_file_path} {classname} -qh")

        # 构建ffmpeg命令
        ffmpeg_command = [
            "ffmpeg",
            "-i",
            "C:\\Users\\frank\\Music\\C418 - Alpha.m4a",  # 音频文件路径
            "-i",
            f"C:\\Users\\frank\\Documents\\E\\pg\\Python\\Manim\\media\\videos\\{filename}\\1080p60\\{classname}.mp4",  # 视频文件路径
            "-map",
            "0:a",  # 选择第一个输入文件的音频流
            "-map",
            "1:v",  # 选择第二个输入文件的视频流
            "-shortest",  # 使输出文件的持续时间与最短的输入流相匹配
            "-y",  # 覆盖输出文件而不询问
            f"{dir_name}\\{classname}.mp4",  # 输出文件路径
        ]

        # 运行ffmpeg命令
        run(ffmpeg_command, check=True)
        startfile(f"{dir_name}\\{classname}.mp4")
    else:
        run(f"manim --save_sections {py_file_path} {classname} -pqh")


class TemplateScene(Scene):
    def signature(self):
        author_name = Text("laialaodi")
        tips = Subtitle.generate_subtitle("tips: 横屏食用观感更佳")
        self.play(Write(author_name), Write(tips))
        self.wait(2)
        self.play(FadeOut(author_name), FadeOut(tips))

    def the_end(self):
        text = Tex("Thanks for watching")
        self.play(Write(text))
        self.wait(2)

    def construct(self):
        self.next_section("signature")
        self.signature()
        self.next_section("the end")
        self.the_end()


class Subtitle:
    @staticmethod
    def generate_subtitle(text: str) -> Tex:
        return Tex(text, font_size=30, tex_template=TexTemplateLibrary.ctex).to_edge(
            DOWN
        )

    def __init__(self, text: str, font_size: int = 30) -> None:
        self.text = text
        self.font_size = font_size
        self.subtitle = self.generate_subtitle(text)

    def show(self, scene: Scene) -> None:
        scene.play(FadeIn(self.subtitle))

    def hide(self, scene: Scene) -> None:
        scene.play(FadeOut(self.subtitle))
