import requests
from google.protobuf.json_format import MessageToDict
from typing import Any, ClassVar, List, Mapping, Optional, Sequence
from typing_extensions import Self
from viam.components.component_base import ValueTypes
from viam.components.sensor import Sensor
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily


class WebSensor(Sensor, Reconfigurable):
    """
    simple web sensor monitor that returns the url and response code
    This sensor is part of a code deploy demo which shows deploying a simple web application
    """
    MODEL: ClassVar[Model] = Model(ModelFamily('shawns-modules', 'web'), 'sensor')
    web_urls: List[str]

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """
        create new instance of web sensor

        :param config:
        :param dependencies:
        :return:
        """
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        """
        validate configuration

        :param config:
        :return:
        """
        web_urls = MessageToDict(config.attributes.fields['web_urls'].list_value)
        if web_urls is None or len(web_urls) == 0:
            raise Exception('web_urls should be an array of urls to check')

        return []

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> None:
        """
        reconfigure component

        :param config:
        :param dependencies:
        :return:
        """
        self.web_urls = MessageToDict(config.attributes.fields['web_urls'].list_value)

    async def get_readings(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Any]:
        """
        TODO: convert to async if needed

        :param extra:
        :param timeout:
        :param kwargs:
        :return:
        """
        reading = {}
        for url in self.web_urls:
            resp = requests.get(url)
            reading[url] = resp.status_code

        return reading

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Mapping[str, ValueTypes]:
        """
        not implemented right now

        :param command:
        :param timeout:
        :param kwargs:
        :return:
        """
        pass


"""
Register the new MODEL as well as define how the object is validated 
and created
"""
Registry.register_resource_creator(
    Sensor.SUBTYPE,
    WebSensor.MODEL,
    ResourceCreatorRegistration(WebSensor.new, WebSensor.validate_config)
)
