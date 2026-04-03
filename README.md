# coova_gha

GitHub Actions workflow to build a `coova-chilli` version `1.8` RPM in a CentOS 6 environment.

## What is included

- `.github/workflows/build-centos6-rpm.yml`: CI workflow that builds RPMs in a `quay.io/centos/centos:6` container.
- `packaging/coova-chilli.spec`: RPM spec for CoovaChilli 1.8.
- `scripts/build-centos6-rpm.sh`: Helper script used by the workflow.

## Triggering the build

Use one of these methods:

- Push to `main`
- Open a pull request
- Manually run `Build CoovaChilli 1.8 RPM (CentOS 6)` from the Actions tab

## Output

The workflow uploads RPMs copied from `/github/home/rpmbuild/` into `artifacts/`:

- Binary RPM(s)
- Source RPM(s)

as artifact `coova-chilli-centos6-rpms`.

## Releases

Built RPMs are also published as GitHub Releases and can be downloaded from:

https://github.com/org3system/coova_gha/releases
