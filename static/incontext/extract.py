from PIL import Image, ImageSequence

def make_gif_loop_forever(input_path, output_path):
    # 打开原始 GIF
    with Image.open(input_path) as im:
        # 收集所有帧和对应的 duration
        frames = []
        durations = []
        for frame in ImageSequence.Iterator(im):
            # 拷贝帧，防止后续处理被覆盖
            frames.append(frame.copy())
            # 获取帧的持续时间（如果没有就给个默认100ms）
            durations.append(frame.info.get('duration', 100))

        # 如果只有1帧，那么本身就没有动画
        if len(frames) == 1:
            print("Warning: Only 1 frame found. This GIF isn't animated.")
            frames[0].save(output_path)
            return

        # 以第一帧为基准，保存多帧GIF
        # save_all=True 允许保存多帧
        # append_images=frames[1:] 把后续所有帧附加进去
        # loop=0 表示无限循环
        # duration=durations 指定每帧的播放时间
        # disposal=2 表示每帧刷新，避免帧重叠出现杂乱
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=durations,
            disposal=2
        )

if __name__ == "__main__":
    import os
    for file in os.listdir("./"):
        if file.endswith(".gif"):
            input_gif = f".//{file}"
            output_gif = f".//{file}"
            make_gif_loop_forever(input_gif, output_gif)
            print(f"已将 {input_gif} 转换为无限循环的 {output_gif}")
