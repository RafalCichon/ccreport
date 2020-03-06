import logging

from ..artifacts.artifact_content_reader import ArtifactContentReader
from ..artifacts.artifact_reader import ArtifactReader
from ..builds.build_definition_reader import BuildDefinitionReader
from ..builds.latest_build_reader import LatestBuildReader
from ..reports.report_xml_reader import ReportXmlReader

logger = logging.getLogger(__name__)


class ReportsCollector:
    def __init__(self, build_client):
        self.__build_client = build_client

    def collect(self, project_name, build_definition_pattern, branch_name):
        logger.info(
            'Collecting code coverage reports for the \'{projectName}\' project.'.format(projectName=project_name)
        )
        reports = []
        definitions = BuildDefinitionReader(self.__build_client)\
            .read(project_name, build_definition_pattern)
        if not definitions:
            logger.info('No build definitions found.')
            return reports
        self.__log_definitions(definitions)
        for d in definitions:
            report = self.__get_report(project_name, d, branch_name)
            reports.append(report)
        return reports

    @staticmethod
    def __log_definitions(definitions):
        logger.info('Found {definitionsCount} definitions:'.format(definitionsCount=len(definitions)))
        for d in definitions:
            logger.info(d.path + '\\' + d.name)

    def __get_report(self, project_name, definition, branch_name):
        result = {
            'line_rate': None,
            'branch_rate': None,
            'definition': definition.path + '\\' + definition.name,
            'build_number': None
        }
        build = self.__get_latest_build(project_name, definition, branch_name)
        if not build:
            return result
        result['build_number'] = build.build_number
        artifact = self.__get_code_coverage_artifact(project_name, build)
        if not artifact:
            return result
        summary_xml = self.__get_summary_xml(project_name, build, artifact)
        if not summary_xml:
            return result
        code_coverage_report = ReportXmlReader.read(summary_xml)
        if not code_coverage_report:
            return result
        result['line_rate'] = code_coverage_report['line_rate']
        result['branch_rate'] = code_coverage_report['branch_rate']
        return result

    def __get_latest_build(self, project_name, definition, branch_name):
        return LatestBuildReader(self.__build_client)\
            .read(project_name, definition, branch_name)

    def __get_code_coverage_artifact(self, project_name, build):
        return ArtifactReader(self.__build_client) \
            .get_code_coverage_artifact(project_name, build)

    def __get_summary_xml(self, project_name, build, artifact):
        artifact_zip_entry_paths = [
            '{artifactName}/summary{buildId}/Cobertura.xml'.format(artifactName=artifact.name, buildId=build.id),
            '{artifactName}/summary{buildId}/coverage.cobertura.xml'.format(artifactName=artifact.name, buildId=build.id)
        ]
        return ArtifactContentReader(self.__build_client) \
            .read(project_name,
                  build,
                  artifact.name,
                  artifact_zip_entry_paths)
