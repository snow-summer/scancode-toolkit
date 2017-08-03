#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

from collections import OrderedDict
import os

from commoncode.testcase import FileBasedTesting
from scancode.license_policy import load_license_policy


class TestLicensePolicy(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_load_license_policy(self):
        assert load_license_policy(None) == {}
        assert load_license_policy('') == {}
        assert load_license_policy('/wrong/path/') == {}
        assert load_license_policy('/') == {}

        expected = OrderedDict([(u'license_policies', 
            OrderedDict([(u'broadcom-commercial', 
                OrderedDict([
                    (u'color_code', u'#FFcc33'), 
                    (u'api_url', u'https://enterprise.dejacode.com/api/v2/usage_policies/0ecccbfc-b87e-40c2-b891-0667560a177c/'), 
                    (u'guidelines', u'These licenses contain obligations...'), 
                    (u'uuid', u'0ecccbfc-b87e-40c2-b891-0667560a177c'), 
                    (u'label', u'Restricted License'), 
                    (u'content_type', u'license'), 
                    (u'icon', u'icon-warning-sign')]))]))])
        
        assert load_license_policy(self.get_test_loc('license_policy/scancode.yml')) == expected