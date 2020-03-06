import xml.etree.ElementTree as xmlElementTree
import logging

logger = logging.getLogger(__name__)


class ReportXmlReader:
    __line_rate_attrib_name = 'line-rate'
    __branch_rate_attrib_name = 'branch-rate'

    @staticmethod
    def read(xml):
        logger.info('Reading the code coverage rate from the xml.')
        tree = ReportXmlReader.__get_tree(xml)
        if not tree:
            return None
        if not tree.tag == 'coverage':
            logger.error('Cannot read the code coverage rate from the xml: no \'coverage\' tag found.')
            return None
        line_rate = float(tree.attrib[ReportXmlReader.__line_rate_attrib_name])\
            if ReportXmlReader.__line_rate_attrib_name in tree.attrib else None
        branch_rate = float(tree.attrib[ReportXmlReader.__branch_rate_attrib_name])\
            if ReportXmlReader.__branch_rate_attrib_name in tree.attrib else None
        logger.info('The code coverage rate from the xml read.')
        return {
            'line_rate': line_rate,
            'branch_rate': branch_rate
        }

    @staticmethod
    def __get_tree(xml):
        try:
            return xmlElementTree.fromstring(xml)
        except TypeError as e:
            logger.error('Error on reading tree from xml string: ' + str(e))
            return None
