# CHANGELOG - External DNS

## 2.2.0 / 2022-05-15

* [Added] Support dynamic bearer tokens (Bound Service Account Token Volume). See [#11915](https://github.com/DataDog/integrations-core/pull/11915).

## 2.1.0 / 2022-04-05 / Agent 7.36.0

* [Added] Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).
* [Fixed] Remove outdated warning in the description for the `tls_ignore_warning` option. See [#11591](https://github.com/DataDog/integrations-core/pull/11591).

## 2.0.0 / 2022-02-19 / Agent 7.35.0

* [Added] Add `pyproject.toml` file. See [#11349](https://github.com/DataDog/integrations-core/pull/11349).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).
* [Changed] Add tls_protocols_allowed option documentation. See [#11251](https://github.com/DataDog/integrations-core/pull/11251).

## 1.5.3 / 2022-01-21 / Agent 7.34.0

* [Fixed] Fix license header dates in autogenerated files. See [#11187](https://github.com/DataDog/integrations-core/pull/11187).

## 1.5.2 / 2022-01-18

* [Fixed] Fix the type of `bearer_token_auth`. See [#11144](https://github.com/DataDog/integrations-core/pull/11144).

## 1.5.1 / 2022-01-08

* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 1.5.0 / 2021-11-13 / Agent 7.33.0

* [Added] Document new include_labels option. See [#10617](https://github.com/DataDog/integrations-core/pull/10617).
* [Added] Document new use_process_start_time option. See [#10601](https://github.com/DataDog/integrations-core/pull/10601).
* [Added] Add controller last sync timestamp metric to external dns. See [#10428](https://github.com/DataDog/integrations-core/pull/10428). Thanks [mattjnewberry](https://github.com/mattjnewberry).

## 1.4.0 / 2021-10-04 / Agent 7.32.0

* [Added] Add runtime configuration validation. See [#8915](https://github.com/DataDog/integrations-core/pull/8915).
* [Added] Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* [Added] Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).
* [Fixed] Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).

## 1.3.0 / 2021-05-28 / Agent 7.29.0

* [Added] Support "ignore_tags" configuration. See [#9392](https://github.com/DataDog/integrations-core/pull/9392).

## 1.2.2 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.2.1 / 2021-01-25 / Agent 7.26.0

* [Fixed] Update prometheus_metrics_prefix documentation. See [#8236](https://github.com/DataDog/integrations-core/pull/8236).

## 1.2.0 / 2020-12-11 / Agent 7.25.0

* [Added] Add config specs. See [#7992](https://github.com/DataDog/integrations-core/pull/7992).

## 1.1.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.0.0 / 2019-12-18 / Agent 7.17.0

* [Added] Add External DNS integration. See [#4340](https://github.com/DataDog/integrations-core/pull/4340). Thanks [davidgibbons](https://github.com/davidgibbons).

## 0.0.2 / 2019-12-04 / Agent 7.16.1

* [Fixed] Fix docs and AD config. See [#5145](https://github.com/DataDog/integrations-core/pull/5145).
