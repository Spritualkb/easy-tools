import re
import sys
import datetime
import asyncio
import aiohttp
import socket
from tqdm import tqdm

async def check_url_alive(url, session):
    try:
        async with session.get(url, timeout=5) as response:
            return response.status == 200
    except:
        return False

async def check_ip_port_alive(ip, port):
    try:
        loop = asyncio.get_running_loop()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            await loop.sock_connect(sock, (ip, int(port)))
            return True
    except:
        return False

async def process_match(match, session, pbar):
    if match.startswith('http'):
        is_alive = await check_url_alive(match, session)
    else:
        ip, port = match.split(':')
        is_alive = await check_ip_port_alive(ip, int(port))
    
    pbar.update(1)
    return match if is_alive else None

async def clean_ip_file(input_filename):
    try:
        with open(input_filename, 'r') as file:
            data = file.read()

        # 正则表达式匹配URL、IP和端口号
        pattern = r'(https?://\d{1,3}(?:\.\d{1,3}){3}:\d{1,5})|(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5})'
        matches = re.findall(pattern, data)

        # 去重
        unique_matches = list(set(match[0] or match[1] for match in matches))

        # 获取当前时间，格式化为 YYYYMMDD_HHMMSS
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f"{current_time}.txt"

        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(unique_matches), desc="检测进度") as pbar:
                tasks = [process_match(match, session, pbar) for match in unique_matches]
                results = await asyncio.gather(*tasks)

        # 将结果写入到新的文件中
        with open(output_filename, 'w') as output_file:
            for result in results:
                if result:
                    output_file.write(result + '\n')

        print(f"提取结果已保存到文件 {output_filename}")

    except FileNotFoundError:
        print(f"文件 {input_filename} 未找到。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python clean.py filename")
    else:
        asyncio.run(clean_ip_file(sys.argv[1]))
