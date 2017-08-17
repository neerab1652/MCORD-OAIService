tosca_definitions_version: tosca_simple_yaml_1_0

# compile this with "m4 oai.m4 > oai.yaml"

# include macros
include(macros.m4)

node_types:
    tosca.nodes.OAIService:
        derived_from: tosca.nodes.Root
        description: >
            OAI Service
        capabilities:
            xos_base_service_caps
        properties:
            xos_base_props
            xos_base_service_props
            
    tosca.nodes.OAITenant:
        derived_from: tosca.nodes.Root
        description: >
            OAI Tenant
        properties:
            xos_base_tenant_props
            tenant_message:
                type: string
                required: false
