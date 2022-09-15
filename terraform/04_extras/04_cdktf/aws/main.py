#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import AwsProvider, ec2


class CDKDemoStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "Aws", region="us-west-2")

        # cdkdemoInstance = ec2.Instance(self, "cdkdemo",
        #                               ami="ami-005e54dee72cc1d00",
        #                               instance_type="t2.micro",
        #                               )

        # TerraformOutput(self, "cdkdemo_public_ip",
        #                value=cdkdemoInstance.public_ip
        #                )


app = App()
CDKDemoStack(app, "cdkdemo-terraform")

app.synth()
