from xosresource import XOSResource
from core.models import Tenant, Service
from services.oai.models import OAITenant

class XOSOAITenant(XOSResource):
    provides = "tosca.nodes.OAITenant"
    xos_model = OAITenant
    copyin_props = ("tenant_message",)
    name_field = None

    def get_xos_args(self, throw_exception=True):
        args = super(XOSOAITenant, self).get_xos_args()

        provider_name = self.get_requirement("tosca.relationships.TenantOfService", throw_exception=throw_exception)
        if provider_name:
            args["provider_service"] = self.get_xos_object(Service, throw_exception=throw_exception, name=provider_name)

        return args

    def get_existing_objs(self):
        args = self.get_xos_args(throw_exception=False)
        provider_service = args.get("provider", None)
        if provider_service:
            return [ self.get_xos_object(provider_service=provider_service) ]
        return []

    def postprocess(self, obj):
        pass

    def can_delete(self, obj):
        return super(XOSOAITenant, self).can_delete(obj)
