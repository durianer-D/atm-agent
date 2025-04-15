import re
import os
import json
import time
import requests
from tqdm import tqdm
from termcolor import colored
import random
from inference.LLM.chatgpt_function_model import ChatGPTFunction
from inference.LLM.davinci_model import Davinci
from inference.LLM.tool_llama_lora_model import ToolLLaMALoRA
from inference.LLM.tool_llama_model import ToolLLaMA
from inference.LLM.retriever import ToolRetriever
from inference.Algorithms.single_chain import single_chain
from inference.Algorithms.DFS import DFS_tree_search
from inference.server import get_rapidapi_response
from utils import (
    standardize,
    change_name,
    replace_llama_with_condense
)

from inference.Downstream_tasks.base_env import base_env


# For pipeline environment preparation
def get_white_list(tool_root_dir):
    # print(tool_root_dir)
    white_list_dir = os.path.join(tool_root_dir)
    white_list = {}
    for cate in tqdm(os.listdir(white_list_dir)):
        if not os.path.isdir(os.path.join(white_list_dir,cate)):
            continue
        for file in os.listdir(os.path.join(white_list_dir,cate)):
            if not file.endswith(".json"):
                continue
            standard_tool_name = file.split(".")[0]
            # print(standard_tool_name)
            with open(os.path.join(white_list_dir,cate,file)) as reader:
                js_data = json.load(reader)
            origin_tool_name = js_data["tool_name"]
            white_list[standardize(origin_tool_name)] = {"description": js_data["tool_description"], "standard_tool_name": standard_tool_name}
    return white_list