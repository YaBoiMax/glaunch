# Maintainer: Your Name <youremail@domain.com>

pkgname=glaunch
pkgver=1.0
pkgrel=1
epoch=1
pkgdesc="A script you can set as a launch command in steam to apply a config. The config is read from ~/.config/games.yml"
arch=('any')
url="https://github.com/YaBoiMax/glaunch"
license=('GPL')
depends=(python)
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
options=()
source=("git+${url}.git")
sha256sums=('SKIP')

package()
{
  cd ${srcdir}/$pkgname
  install -Dm755 main.py "$pkgdir/usr/bin/glaunch"
}
