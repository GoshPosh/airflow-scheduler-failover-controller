
class Stats:
    def __init__(self, configuration, logger):
        self._stats_on = configuration.get_airflow_statsd_on()
        if self._stats_on:
            from statsd import StatsClient
            self._stats = StatsClient(
                host=configuration.get_airflow_statsd_host(),
                port=configuration.get_airflow_statsd_port(),
                prefix=configuration.get_airflow_statsd_prefix())
        else:
            logger.info('stats_on is set to False in [scheduler], ignoring statsd monitoring.')

    def increment(self, metric, value=1, sample_rate=1):
        if self._stats_on:
            self._stats.incr(metric, value, sample_rate)
