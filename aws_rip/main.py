import os
import tomllib
from aws_cdk import (
    Stack,
    aws_codecommit as code_commit,
    pipelines as pipelines
)
from constructs import Construct

def load_config():
    with open('./config.toml') as config_file: 
        content = config_file.read()
        config = tomllib.loads(content)

        # attempt to parse config
        match config:
            case {'repo_name': str(), 'pipeline_name': str(), 'deployable': bool()}:
                return config
            case other:
                raise ValueError(f'Invalid config: {config}')


class RIP(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        config = load_config()
        repo_name = config['repo_name']

        # Resources 
        repo = code_commit.Repository(
            self,
            repo_name,
            repository_name=repo_name,
        )

        pipeline = pipelines.CodePipeline(
            self,
            config['pipeline_name'],
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"),
                commands=[
                    'npm install -g aws-cdk',
                    # Install poetry to install deps
                    'curl -sSL https://install.python-poetry.org | python3 -',
                    'poetry install',
                    'cdk synth',
                ]
            ),
        )

        if config['deployable']:
            deploy_stage = PipelineStage(self, "deploy")
            add_deploy_stage = pipeline.add_stage(deploy_stage)
