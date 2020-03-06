from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import logging
from .reports.reports_collector import ReportsCollector


def collect(args):
    logger = logging.getLogger(__name__)

    credentials = BasicAuthentication('', args.token)
    connection = Connection(base_url=args.organization_url, creds=credentials)

    build_client = connection.clients_v6_0.get_build_client()

    reports = ReportsCollector(build_client)\
        .collect(args.project_name, args.definition_pattern, args.branch_name)

    if not reports:
        logger.info('Summary: no reports found')
    else:
        logger.info('Summary:')
        for r in reports:
            line_coverage_rate = r['line_rate']
            branch_coverage_rate = r['branch_rate']
            build_number = r['build_number']
            logger.info(
                '{definitionName} - {buildNumber} - line: {line}%, branch: {branch}%'
                .format(definitionName=r['definition'],
                        buildNumber=build_number if build_number else '<no latest build>',
                        line=round(line_coverage_rate * 100, 2) if line_coverage_rate else '--',
                        branch=round(branch_coverage_rate * 100, 2) if branch_coverage_rate else '--')
            )
