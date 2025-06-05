# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from aiq.builder.builder import Builder
from aiq.cli.register_workflow import register_memory
from aiq.data_models.memory import MemoryBaseConfig


class Mem0BuildNvidiaMemoryClientConfig(MemoryBaseConfig, name="mem0_build_nvidia"):
    vec_store_provider: str = "milvus"  # Change to "qdrant" if you prefer that
    vec_store_collection_name: str = "DefaultAIQCollection"
    vec_store_url: str = "http://localhost:19530"  # Default Milvus URL, change if needed
    vec_store_embedding_model_dims: int = 768  # Change this according to your local model's dimensions
    llm_provider: str = "ollama"
    llm_model: str = "command-r7b:latest"  # Change to your preferred model
    llm_temperature: float = 0.0
    llm_max_tokens: int = 2000
    llm_base_url: str = "http://localhost:11434"  # Default Ollama URL, change if needed
    embedder_provider: str = "ollama"
    embedder_model: str = "snowflake-arctic-embed2:latest"
    embedder_base_url: str = "http://localhost:11434"  # Default Ollama URL, change if needed


@register_memory(config_type=Mem0BuildNvidiaMemoryClientConfig)
async def mem0_memory_client(config: Mem0BuildNvidiaMemoryClientConfig, builder: Builder):
    import os

    from mem0 import Memory

    from aiq.plugins.mem0ai.mem0_editor import Mem0Editor

    config = {
        "vector_store": {
            "provider": config.vec_store_provider,
            "config": {
                "collection_name": config.vec_store_collection_name,
                "url": config.vec_store_url,
                "embedding_model_dims": config.vec_store_embedding_model_dims,
            },
        },
        "llm": {
            "provider": "langchain",
            "config": {
                # choose an llm model from build.nvidia.com
                "model": "llama3.1:latest",
                "temperature": 0,
                "max_tokens": 2000,
                "base_url": "https://integrate.api.nvidia.com/v1",  # Ensure this URL is correct
            },
        },
        "embedder": {
            "provider": "langchain",
            "config": {
                # choose an embedding model from build.nvidia.com
                "model": "snowflake-arctic-embed2:latest",
                "base_url": "https://integrate.api.nvidia.com/v1",
            },
        },
    }
    
    # Initialize Memory with the configuration
    mem0_client = Memory.from_config(config)

    memory_editor = Mem0Editor(mem0_client=mem0_client)

    yield memory_editor