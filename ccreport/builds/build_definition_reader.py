from ..builds.build_definitions_filter import BuildDefinitionsFilter


class BuildDefinitionReader:
    def __init__(self, build_client):
        self.__build_client = build_client

    def read(self, project_name, build_definition_pattern):
        definitions = self.__build_client.get_definitions(project_name)
        definitions = BuildDefinitionsFilter.filter(definitions, build_definition_pattern)
        definitions.sort(key=lambda d: d.path + '\\' + d.name)
        return definitions
