# -*- coding: utf-8 -*-


class ElementFinder(object):

    def __init__(self):
        self._strategies = {
            'identifier': self._find_by_identifier,
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'dom': self._find_by_dom,
            'link': self._find_by_link_text,
            'partial link': self._find_by_partial_link_text,
            'css': self._find_by_css_selector,
            'jquery': self._find_by_sizzle_selector,
            'sizzle': self._find_by_sizzle_selector,
            'tag': self._find_by_tag_name,
            'scLocator': self._find_by_sc_locator,
            'default': self._find_by_default
        }

    def find(self, driver, locator, tag=None):
        assert driver is not None
        assert locator is not None and len(locator) > 0

        (prefix, criteria) = self._parse_locator(locator)
        prefix = 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        (tag, constraints) = self._get_tag_and_constraints(tag)
        return strategy(driver, criteria, tag, constraints)

    # Strategy routines, private

    def _find_by_identifier(self, driver, criteria, tag, constraints):
        elements = self._normalize_result(driver.find_elements_by_id(criteria))
        elements.extend(self._normalize_result(driver.find_elements_by_name(criteria)))
        return self._filter_elements(elements, tag, constraints)

    def _find_by_id(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_id(criteria), tag, constraints)

    def _find_by_name(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_name(criteria),
            tag, constraints)

    def _find_by_xpath(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_xpath(criteria),
            tag, constraints)

    def _find_by_dom(self, driver, criteria, tag, constraints):
        result = driver.execute_script("return %s;" % criteria)
        if result is None:
            return []
        if not isinstance(result, list):
            result = [result]
        return self._filter_elements(result, tag, constraints)

    def _find_by_sizzle_selector(self, driver, criteria, tag, constraints):
        js = "return jQuery('%s').get();" % criteria.replace("'", "\\'")
        return self._filter_elements(
            driver.execute_script(js),
            tag, constraints)

    def _find_by_link_text(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_link_text(criteria),
            tag, constraints)

    def _find_by_partial_link_text(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_partial_link_text(criteria),
            tag, constraints)

    def _find_by_css_selector(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_css_selector(criteria),
            tag, constraints)

    def _find_by_tag_name(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_tag_name(criteria),
            tag, constraints)

    def _find_by_sc_locator(self, driver, criteria, tag, constraints):
        js = "return isc.AutoTest.getElement('%s')" % criteria.replace("'", "\\'")
        return self._filter_elements([driver.execute_script(js)], tag, constraints)

    def _find_by_default(self, driver, criteria, tag, constraints):
        if criteria.startswith('//'):
            return self._find_by_xpath(driver, criteria, tag, constraints)
        return self._find_by_key_attrs(driver, criteria, tag, constraints)

    def __escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value

    def _find_by_key_attrs(self, driver, criteria, tag, constraints):
        key_attrs = self._key_attrs.get(None)
        if tag is not None:
            key_attrs = self._key_attrs.get(tag, key_attrs)

        xpath_criteria = self.__escape_xpath_value(criteria)
        xpath_tag = tag if tag is not None else '*'
        xpath_constraints = ["@%s='%s'" % (name, constraints[name]) for name in constraints]
        xpath_searchers = ["%s=%s" % (attr, xpath_criteria) for attr in key_attrs]
        xpath_searchers.extend(
            self._get_attrs_with_url(key_attrs, criteria, driver))
        xpath = "//%s[%s(%s)]" % (
            xpath_tag,
            ' and '.join(xpath_constraints) + ' and ' if len(xpath_constraints) > 0 else '',
            ' or '.join(xpath_searchers))

        return self._normalize_result(driver.find_elements_by_xpath(xpath))

    # Private

    _key_attrs = {
        None: ['@id', '@name'],
        'a': ['@id', '@name', '@href', 'normalize-space(descendant-or-self::text())'],
        'img': ['@id', '@name', '@src', '@alt'],
        'input': ['@id', '@name', '@value', '@src'],
        'button': ['@id', '@name', '@value', 'normalize-space(descendant-or-self::text())']
    }

    def _get_tag_and_constraints(self, tag):
        if tag is None: return None, {}

        tag = tag.lower()
        constraints = {}
        if tag == 'link':
            tag = 'a'
        if tag == 'partial link':
            tag = 'a'
        elif tag == 'image':
            tag = 'img'
        elif tag == 'list':
            tag = 'select'
        elif tag == 'radio button':
            tag = 'input'
            constraints['type'] = 'radio'
        elif tag == 'checkbox':
            tag = 'input'
            constraints['type'] = 'checkbox'
        elif tag == 'text field':
            tag = 'input'
            constraints['type'] = 'text'
        elif tag == 'file upload':
            tag = 'input'
            constraints['type'] = 'file'
        elif tag == 'text area':
            tag = 'textarea'
        return tag, constraints

    def _element_matches(self, element, tag, constraints):
        if not element.tag_name.lower() == tag:
            return False
        for name in constraints:
            if not element.get_attribute(name) == constraints[name]:
                return False
        return True

    def _filter_elements(self, elements, tag, constraints):
        elements = self._normalize_result(elements)
        if tag is None: return elements
        return filter(
            lambda element: self._element_matches(element, tag, constraints),
            elements)

    def _get_attrs_with_url(self, key_attrs, criteria, browser):
        attrs = []
        url = None
        xpath_url = None
        for attr in ['@src', '@href']:
            if attr in key_attrs:
                if url is None or xpath_url is None:
                    url = self._get_base_url(browser) + "/" + criteria
                    xpath_url = self.__escape_xpath_value(url)
                attrs.append("%s=%s" % (attr, xpath_url))
        return attrs

    def _get_base_url(self, browser):
        url = browser.get_current_url()
        if '/' in url:
            url = '/'.join(url.split('/')[:-1])
        return url

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return (prefix, criteria)

    def _normalize_result(self, elements):
        if not isinstance(elements, list):
            return []
        return elements

    def escape_xpath_value(self, value):
        if '"' in value and '\'' in value:
            parts_wo_apos = value.split('\'')
            return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
        if '\'' in value:
            return "\"%s\"" % value
        return "'%s'" % value

elementFinder = ElementFinder()
