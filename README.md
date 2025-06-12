# 🟩 Nvidia AgentIQ toolkit 🔌 Mem0 Plugin Extended Integration Scripts

These are example scripts for Nvidia AgentIQ for configuring Mem0 with local sources and has been updated for the V2 version of Mem0 with a new plugin integration. This will allow you to run a local Nvidia AgentIQ memory development config, so that your agent will remember your preferences based on your user_id.

This version was setup for Milvus vector store running locally, Mem0 installed locally, and several instances of ollama running locally for embedding and llm commands (need a tool calling model).

This is for demonstration purposes only and not a complete package. You must have the original package for this to work.

## Important Files

* mem0_editor.py - a hevily modified version of the original to support Mem0 V2 API
* memory_local.py - new version for connecting to local resources like local Milvus and Ollama

Mem0 config field list are listed in Mem0_core_configuration_options.md

## Installation plan

These files are ment to be copied into <aiq folder>/packages/aiqtoolkit_mem0ai/src/aiq/plugins/mem0ai  
Best practice not to overwrite the original memory.py and mem0_editor.py incase of future aiq repo updates.  

You will have to add this import to register.py: from . import memory_local_ollama  

Once these files copied into your plugin folder, you'll have to reload to plugin. You can call these configuration by using the following commands:  

Go to the aiqtoolkit_mem0ai plugin main folder, and install like any workflow:  

uv pip install -e .  

To view if it is installed, use the command:  

aiq info components -q "memory" 

## Workflow Config updates

There is a sample config folder that shows how I used the config to setup the file for my local use. Please modify the memory and llm section to point to your local instances. 

## Links

More information on using memory in agentiq can be found here:

Nvidia AgentIQ Documentation - https://docs.nvidia.com/agentiq/latest/index.html  
Mem0 Documentation - https://docs.mem0.ai/overview  
Nvidia NGC - https://ngc.nvidia.com  
Nvidia Build - https://build.nvidia.com  
Quadrant - https://qdrant.tech  
Ollama - https://ollama.com  

## Acknowledgments

This project is based on the original aiqtoolkit_mem0ai plugin Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved. Licensed under the Apache License 2.0.  
  
Modifications and enhancements (c) 2025 Jeremy Kesten.  
  
Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at  
  
http://www.apache.org/licenses/LICENSE-2.0  
  
Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and  
limitations under the License.  