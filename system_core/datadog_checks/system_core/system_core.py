# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import psutil
from six import iteritems

from datadog_checks.base.utils.platform import Platform
from datadog_checks.base import AgentCheck


class SystemCore(AgentCheck):
    def check(self, instance):
        instance_tags = instance.get('tags', [])

        # https://psutil.readthedocs.io/en/latest/#psutil.cpu_count
        n_cpus = psutil.cpu_count()
        self.gauge('system.core.count', n_cpus, tags=instance_tags)

        # https://psutil.readthedocs.io/en/latest/#psutil.cpu_times
        cpu_times = psutil.cpu_times(percpu=True)

        for i, cpu in enumerate(cpu_times):
            tags = instance_tags + ['core:{0}'.format(i)]
            for key, value in iteritems(cpu._asdict()):
                self.rate('system.core.{0}'.format(key), value, tags=tags)

        cpu_times_total = psutil.cpu_times()
        for key, value in iteritems(cpu_times_total._asdict()):
            self.rate('system.core.{0}.total'.format(key), value, tags=instance_tags)

        # https://psutil.readthedocs.io/en/latest/#psutil.cpu_freq
        # scpufreq(current=2236.812, min=800.0, max=3500.0)
        # Ignore min/max as they are often reported as 0.0 if undetermined.
        cpu_freq = psutil.cpu_freq(percpu=True)
        for i, cpu in enumerate(cpu_freq):
            if Platform.is_unix():
                # Per-cpu frequency retrieval (Linux only)
                tags = instance_tags + ['core:{0}'.format(i)]
            self.gauge('system.core.frequency', cpu._asdict().get('current'), tags=tags)
