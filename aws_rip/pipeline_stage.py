from constructs import Construct
from aws_cdk import (
   Stage 
)

class PipelineStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super.__init__(scope, id, **kwargs)
        
        # Define infrastructure here
