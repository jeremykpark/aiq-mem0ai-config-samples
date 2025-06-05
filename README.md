# 🟩 Nvidia AgentIQ toolkit 🔌 Mem0 Plugin Extended Integration Scripts

These are example scripts for Nvidia AgentIQ for configuring Mem0 with other sources than the cloud version. Two included additional plugins for local setup (for connecting to local Milvus, qdrant, NIMs or Ollama ) or for using build.nvidia.com models.

## Important Files

These files are ment to run in <aiq folder>/packages/aiqtoolkit_mem0ai/src/aiq/plugins/mem0ai

* memory.py - the original version for connecting to mem0 cloud
* mem0_editor.py - the original version
* memory_local.py - new version for connecting to local resources like Quadrant, Nvidia NIMs and Ollama
* memory_nvidia_build.py - new version for connecting to build.nvidia.com
* register.py - updated with additional files

Mem0 config field list are listed in Mem0_core_configuration_options.md

## Installation plan

Once these files copied into your plugin folder, you'll have to reload to plugin. You can call these configuration by using the following commands:

Go to the aiqtoolkit_mem0ai plugin main folder, and install like any workflow:

uv install -e . 

To view if it is installed, use the command:

aiq info components -q "memory"

## Workflow Config updates

Update your workflows config with the following options:



## How to use in workflow




More information on using memory in agentiq can be found here:

## Links

Nvidia AgentIQ Documentation - https://docs.nvidia.com/agentiq/latest/index.html  
Mem0 Documentation - https://docs.mem0.ai/overview  
Nvidia NGC - https://ngc.nvidia.com  
Nvidia Build - https://build.nvidia.com  
Quadrant - https://qdrant.tech  
Ollama - https://ollama.com  

## Contributors

Created by Jeremy Kesten in 2025 for public use with the Nvidia AgentIQ Toolkit
