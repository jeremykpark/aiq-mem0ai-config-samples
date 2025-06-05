## Nvidia AgentIQ toolkit Mem0 Plugin Extended Integration Scripts

These are example scripts for Nvidia AgentIQ for configuring Mem0 with other sources than the cloud version. Included Local Ollama/Quadrant, Nvidia NGC or Nvidia Build.

# Important Files

These files are ment to run in <aiq folder>/packages/aiqtoolkit_mem0ai/src/aiq/plugins/mem0ai

memory.py - the original version
memory_local.py - new version for connecting to local resources like Quadrant and Ollama
memory_nvidia_build.py - new version for connecting to build.nvidia.com
memory_nvidia_ngc.py - new version for connecting to Nvidia NGC

# Installation plan

Once these files copied into your plugin folder, you'll have to reload to plugin. You can call these configuration by using the following commands:
