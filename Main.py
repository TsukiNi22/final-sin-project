import base64
import lzma
import ast
import os

__Develloper__ = False
__Devellopement__ = True
__Key__ = '/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AfFBsBdAAYfCqEd3CDfTn0EdQwG9IMVj9wGPb/vZHr8Ld8oagsYbdBxkV7wNjXctBYzpdkduFyPhrh+2Y02Y1M+zDDyiW8+zJSEg6kvMAt2w5KCQXtd30AvH3FZ+wGRJcCv2dtbHWyqm05qPyDm1m/VOUazBwMVpnjfMFmsLHrQs9w1BmXSp+kRrYnc25mvO65D4jzOW0QwoewhjS1NuIiZhJjxuUTc8zR4aKe12KAWaj1rnkuHfe4SKSl5xDzaJkCp/5/8CUyfCsAiMDS6Tn67GKyYDDCYzVib2yhLSt41lDlDpNPECf6XxS0Kq8QghxgSXu2COykYbz+oBjQ6a+sKNMmuW8g4GbItmBmc4hILlpO/hO3uux804I1F5dBtJt46xgEkc7gR8XVp7vXnbaVd7GB6dQIaVYwMu5jvQqhpPQPgqIPzUEaEUGAPRdIUDN7qdPsbdB24pIwsqe7e0uopxO+v5JwEGjWrNKB6tgcL6flNLKsrKZDFeocKmY4GJJaMckpcKqRrQ63fdw7KHrknOZetWS6ZaXgVvM8u9+ZpYhoiwQcdX1og7hnkaXN7WUip0D8QDgivcM2mZ+aJnHheInEq80kRc4C8/Pcaby5A/9Cn4rh17HzIKSycJ8db1mA2le9Hj9xQ7jpcD17vu0HUIfLvC98zgfxHuNBPZuBxe0G/sS26o7rPw9m84R8R4i+soLJgsQBFTqDhy7FpCUifNx9bVOfbYeLT7LIWZbfKpSKzAsPFFlBStcdNkwwL5+SccjK273QXwhb6WrnmPrEcO4jQYBwLitV/ZHDVkFhpa/G0KNpg6LDQrjTWu8ewRGSslAW732ckRvhtISd/Xb1pJ5pkPcYM2+NgkJkEfnmdLawSXU7C14OOcTdL6b1c19SkKlXtuO9hjGjcdNKYas9SSoyhJeinnfL7LVQVAN5V1h9qWtqekSoor5GOtJJDW1xjwY29ZSYQtxd89BgK541aTXYOrutLHiHTQNm6pmonkPkD7ps8YYPRAeoAIMoOh5vui9v0Xg7RpDmY58CORqnX2rVHwhQAW/wFAUCIaOB7z0p8q05rw16MZ/Ktrghwsp6rDkSAVtUUes0TiGbB2APGimemVTOG1WNfKeCDO3kJpClI/FQMT6L4U6yk+lnoiewHLeiTfs4VpSWQ8TXNTPBoL8l5awhBM8H/kw1N8KHYK9Pr8sLllhWL4/O4haouh1bJplAKXxWi5nGzdjEQg3D8U0i7VDiohXmdgX4jMapnbSmqqvvFl6wa1uAqeQEI0nsjOtizoJxhMTwQO9V3fvus1kstoJtqZVcCK70ivvTmFMmNye2MMMimYaKu6rNlZfYP8uZvLyxd+J20qq5I67I0R6jyfA2YnlJYpfRJauDUIPaKtONDW2+ZfApYDGD8ipkfxobmvS6IuF14AlOGh3x/5Gz66eWparcx3zpJM36u2qFNwAIBjo3QtnHnVi6szhsFaZ+O7aZ38jRx6jUhp80+DOsXB45Fo96L+c1ila85UZ2dQ8EnwO+r1ygmm/I4N/wBTC1cG5Lep5FxP+8MTatE6JgCfis3eCwJ/yqkQ4/CCCwgmAmCd9tP4hDGG7M7y4fqZEdAUwXnK5A1uaWJgIutVbagLRuchfSKA5giJK3xof9AnOrUqkKP4kfWk9140YBMKd4w0kW8FEnm4DKg5/E9z65nMgA+sSkByyDAIdG+m4Wzs0avAlHIUSgICyxJ20nf3lC7Z9CTIIaDlNBk1WTKnZNtNA03XMR5QeU43fWzphP9zxsdUdNVate7Wg2kJ7bGWjCXCMBNf1ekj2qNi8q+JDZMHMHXEafwxQROBT3UFA7O3DBM4ugT1f8M9H29+SB/lRTQ5Ky6lDxUU3/cyb0127KAD77iAbe66zrAXbQ6Y4wkbuFY/uFXuIntjPDyETeZhpDNntWH10fEoWb+bWHu48G+Bvnc+LHSUQEN8aONQVBSAfZPJBa6mbIYsd2oT+bSkIxueXJzBmiOi0FNKwxM3Qb0MtUBkeKJ+9D6apP7uFAOXefX/U8B948KxkPpkYZCy6Rk6jXHJ8X8m7LK2fFV9Dh2c7fzMP63DVsbog59CKhiTrsXltzvzQLjq92p3HiFj6Tr2xSiLeziW+58V9D0rcUfBdr/xSOR3CcbQN3tMQzZuQiBE1piblFOyT5pHODwDDjB/uP4c0hgX/s62TT6eF6iCCCxmM+8y774Vu1kOMpYK1ZppP7nXXXouwsTvBKUIxy1EORxkUl/ZCV4pVDUHG9iCttFnR57aJAY33vSnj8rJutgiI8u3WAM76TC85Kr0GKqAAADMrZMJ3Ge0AAB3A3GDwAA3zpDBrHEZ/sCAAAAAARZWg=='

List_File = ['Redirect.py', 'Arduino.py', 'Class.py', 'Test.py',
     'img\\Blank.png', 'img\\Branchement.PNG', 'img\\Button.PNG', 'img\\Magic_3_-removebg-preview.ico', 'img\\Potentiometre.png',
     'video\\Flash Bang Easter.mp4', 'video\\Flash bang sound.mp4', 'video\\Logo.mp4', 'video\\Sound1.mp4',
     'txt\\Commande_Boutton.txt', 'txt\\Commande_Potentiometre.txt', 'txt\\Key_Encode.txt',
     'tools\\Encode.py', 'tools\\langages.py', 'tools\\Tools.py', 'tools\\Pip.py',
     'arduino\\arduino-cli.exe', 'arduino\\arduino.ino',
     'lib\\TkVideoPlayer.py',
     'file_copy\\psutil\\.gitignore', 'file_copy\\psutil\\appveyor.yml', 'file_copy\\psutil\\CONTRIBUTING.md', 'file_copy\\psutil\\CREDITS', 'file_copy\\psutil\\HISTORY.rst', 'file_copy\\psutil\\INSTALL.rst', 'file_copy\\psutil\\LICENSE', 'file_copy\\psutil\\make.bat', 'file_copy\\psutil\\Makefile', 'file_copy\\psutil\\MANIFEST.in', 'file_copy\\psutil\\pyproject.toml', 'file_copy\\psutil\\README.rst', 'file_copy\\psutil\\SECURITY.md', 'file_copy\\psutil\\setup.py', 'file_copy\\pycaw\\callbacks.py', 'file_copy\\pycaw\\constants.py', 'file_copy\\pycaw\\magic.py', 'file_copy\\pycaw\\pycaw.py', 'file_copy\\pycaw\\utils.py', 'file_copy\\pycaw\\__init__.py', 'file_copy\\psutil\\.github\\FUNDING.yml', 'file_copy\\psutil\\.github\\no-response.yml', 'file_copy\\psutil\\.github\\placeholder', 'file_copy\\psutil\\.github\\PULL_REQUEST_TEMPLATE.md', 'file_copy\\psutil\\docs\\.readthedocs.yaml', 'file_copy\\psutil\\docs\\conf.py', 'file_copy\\psutil\\docs\\DEVGUIDE.rst', 'file_copy\\psutil\\docs\\DEVNOTES', 'file_copy\\psutil\\docs\\index.rst', 'file_copy\\psutil\\docs\\make.bat', 'file_copy\\psutil\\docs\\Makefile', 'file_copy\\psutil\\docs\\README', 'file_copy\\psutil\\docs\\requirements.txt', 'file_copy\\psutil\\psutil\\_common.py', 'file_copy\\psutil\\psutil\\_compat.py', 'file_copy\\psutil\\psutil\\_psaix.py', 'file_copy\\psutil\\psutil\\_psbsd.py', 'file_copy\\psutil\\psutil\\_pslinux.py', 'file_copy\\psutil\\psutil\\_psosx.py', 'file_copy\\psutil\\psutil\\_psposix.py', 'file_copy\\psutil\\psutil\\_pssunos.py', 'file_copy\\psutil\\psutil\\_psutil_aix.c', 'file_copy\\psutil\\psutil\\_psutil_bsd.c', 'file_copy\\psutil\\psutil\\_psutil_common.c', 'file_copy\\psutil\\psutil\\_psutil_common.h', 'file_copy\\psutil\\psutil\\_psutil_linux.c', 'file_copy\\psutil\\psutil\\_psutil_osx.c', 'file_copy\\psutil\\psutil\\_psutil_posix.c', 'file_copy\\psutil\\psutil\\_psutil_posix.h', 'file_copy\\psutil\\psutil\\_psutil_sunos.c', 'file_copy\\psutil\\psutil\\_psutil_windows.c', 'file_copy\\psutil\\psutil\\_pswindows.py', 'file_copy\\psutil\\psutil\\__init__.py', 'file_copy\\psutil\\scripts\\battery.py', 'file_copy\\psutil\\scripts\\cpu_distribution.py', 'file_copy\\psutil\\scripts\\disk_usage.py', 'file_copy\\psutil\\scripts\\fans.py', 'file_copy\\psutil\\scripts\\free.py', 'file_copy\\psutil\\scripts\\ifconfig.py', 'file_copy\\psutil\\scripts\\iotop.py', 'file_copy\\psutil\\scripts\\killall.py', 'file_copy\\psutil\\scripts\\meminfo.py', 'file_copy\\psutil\\scripts\\netstat.py', 'file_copy\\psutil\\scripts\\nettop.py', 'file_copy\\psutil\\scripts\\pidof.py', 'file_copy\\psutil\\scripts\\pmap.py', 'file_copy\\psutil\\scripts\\procinfo.py', 'file_copy\\psutil\\scripts\\procsmem.py', 'file_copy\\psutil\\scripts\\ps.py', 'file_copy\\psutil\\scripts\\pstree.py', 'file_copy\\psutil\\scripts\\sensors.py', 'file_copy\\psutil\\scripts\\temperatures.py', 'file_copy\\psutil\\scripts\\top.py', 'file_copy\\psutil\\scripts\\who.py', 'file_copy\\psutil\\scripts\\winservices.py', 'file_copy\\pycaw\\api\\__init__.py', 'file_copy\\pycaw\\__pycache__\\callbacks.cpython-39.pyc', 'file_copy\\pycaw\\__pycache__\\constants.cpython-39.pyc', 'file_copy\\pycaw\\__pycache__\\magic.cpython-39.pyc', 'file_copy\\pycaw\\__pycache__\\pycaw.cpython-39.pyc', 'file_copy\\pycaw\\__pycache__\\utils.cpython-39.pyc', 'file_copy\\pycaw\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\psutil\\.github\\ISSUE_TEMPLATE\\bug.md', 'file_copy\\psutil\\.github\\ISSUE_TEMPLATE\\config.yml', 'file_copy\\psutil\\.github\\ISSUE_TEMPLATE\\enhancement.md', 'file_copy\\psutil\\.github\\workflows\\bsd.yml', 'file_copy\\psutil\\.github\\workflows\\build.yml', 'file_copy\\psutil\\.github\\workflows\\issues.py', 'file_copy\\psutil\\.github\\workflows\\issues.yml', 'file_copy\\psutil\\docs\\_static\\copybutton.js', 'file_copy\\psutil\\docs\\_static\\favicon.ico', 'file_copy\\psutil\\docs\\_static\\logo.png', 'file_copy\\psutil\\docs\\_static\\pmap-small.png', 'file_copy\\psutil\\docs\\_static\\pmap.png', 'file_copy\\psutil\\docs\\_static\\procinfo-small.png', 'file_copy\\psutil\\docs\\_static\\procinfo.png', 'file_copy\\psutil\\docs\\_static\\procsmem-small.png', 'file_copy\\psutil\\docs\\_static\\procsmem.png', 'file_copy\\psutil\\docs\\_static\\psutil-logo.png', 'file_copy\\psutil\\docs\\_static\\sidebar.js', 'file_copy\\psutil\\docs\\_static\\tidelift-logo.svg', 'file_copy\\psutil\\docs\\_static\\top-small.png', 'file_copy\\psutil\\docs\\_static\\top.png', 'file_copy\\psutil\\psutil\\tests\\README.rst', 'file_copy\\psutil\\psutil\\tests\\runner.py', 'file_copy\\psutil\\psutil\\tests\\test_aix.py', 'file_copy\\psutil\\psutil\\tests\\test_bsd.py', 'file_copy\\psutil\\psutil\\tests\\test_connections.py', 'file_copy\\psutil\\psutil\\tests\\test_contracts.py', 'file_copy\\psutil\\psutil\\tests\\test_linux.py', 'file_copy\\psutil\\psutil\\tests\\test_memleaks.py', 'file_copy\\psutil\\psutil\\tests\\test_misc.py', 'file_copy\\psutil\\psutil\\tests\\test_osx.py', 'file_copy\\psutil\\psutil\\tests\\test_posix.py', 'file_copy\\psutil\\psutil\\tests\\test_process.py', 'file_copy\\psutil\\psutil\\tests\\test_process_all.py', 'file_copy\\psutil\\psutil\\tests\\test_sunos.py', 'file_copy\\psutil\\psutil\\tests\\test_system.py', 'file_copy\\psutil\\psutil\\tests\\test_testutils.py', 'file_copy\\psutil\\psutil\\tests\\test_unicode.py', 'file_copy\\psutil\\psutil\\tests\\test_windows.py', 'file_copy\\psutil\\psutil\\tests\\__init__.py', 'file_copy\\psutil\\psutil\\tests\\__main__.py', 'file_copy\\psutil\\scripts\\internal\\appveyor_run_with_compiler.cmd', 'file_copy\\psutil\\scripts\\internal\\bench_oneshot.py', 'file_copy\\psutil\\scripts\\internal\\bench_oneshot_2.py', 'file_copy\\psutil\\scripts\\internal\\check_broken_links.py', 'file_copy\\psutil\\scripts\\internal\\clinter.py', 'file_copy\\psutil\\scripts\\internal\\convert_readme.py', 'file_copy\\psutil\\scripts\\internal\\download_wheels_appveyor.py', 'file_copy\\psutil\\scripts\\internal\\download_wheels_github.py', 'file_copy\\psutil\\scripts\\internal\\generate_manifest.py', 'file_copy\\psutil\\scripts\\internal\\git_pre_commit.py', 'file_copy\\psutil\\scripts\\internal\\print_access_denied.py', 'file_copy\\psutil\\scripts\\internal\\print_announce.py', 'file_copy\\psutil\\scripts\\internal\\print_api_speed.py', 'file_copy\\psutil\\scripts\\internal\\print_dist.py', 'file_copy\\psutil\\scripts\\internal\\print_downloads.py', 'file_copy\\psutil\\scripts\\internal\\print_hashes.py', 'file_copy\\psutil\\scripts\\internal\\print_timeline.py', 'file_copy\\psutil\\scripts\\internal\\purge_installation.py', 'file_copy\\psutil\\scripts\\internal\\README', 'file_copy\\psutil\\scripts\\internal\\winmake.py', 'file_copy\\pycaw\\api\\audioclient\\depend.py', 'file_copy\\pycaw\\api\\audioclient\\__init__.py', 'file_copy\\pycaw\\api\\audiopolicy\\__init__.py', 'file_copy\\pycaw\\api\\endpointvolume\\depend.py', 'file_copy\\pycaw\\api\\endpointvolume\\__init__.py', 'file_copy\\pycaw\\api\\mmdeviceapi\\__init__.py', 'file_copy\\pycaw\\api\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\psutil\\docs\\_static\\css\\custom.css', 'file_copy\\psutil\\psutil\\arch\\aix\\common.c', 'file_copy\\psutil\\psutil\\arch\\aix\\common.h', 'file_copy\\psutil\\psutil\\arch\\aix\\ifaddrs.c', 'file_copy\\psutil\\psutil\\arch\\aix\\ifaddrs.h', 'file_copy\\psutil\\psutil\\arch\\aix\\net_connections.c', 'file_copy\\psutil\\psutil\\arch\\aix\\net_connections.h', 'file_copy\\psutil\\psutil\\arch\\aix\\net_kernel_structs.h', 'file_copy\\psutil\\psutil\\arch\\bsd\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\bsd\\cpu.h', 'file_copy\\psutil\\psutil\\arch\\bsd\\disk.c', 'file_copy\\psutil\\psutil\\arch\\bsd\\disk.h', 'file_copy\\psutil\\psutil\\arch\\bsd\\net.c', 'file_copy\\psutil\\psutil\\arch\\bsd\\net.h', 'file_copy\\psutil\\psutil\\arch\\bsd\\proc.c', 'file_copy\\psutil\\psutil\\arch\\bsd\\proc.h', 'file_copy\\psutil\\psutil\\arch\\bsd\\sys.c', 'file_copy\\psutil\\psutil\\arch\\bsd\\sys.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\cpu.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\disk.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\disk.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\mem.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\mem.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\proc.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\proc.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\proc_socks.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\proc_socks.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\sensors.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\sensors.h', 'file_copy\\psutil\\psutil\\arch\\freebsd\\sys_socks.c', 'file_copy\\psutil\\psutil\\arch\\freebsd\\sys_socks.h', 'file_copy\\psutil\\psutil\\arch\\linux\\disk.c', 'file_copy\\psutil\\psutil\\arch\\linux\\disk.h', 'file_copy\\psutil\\psutil\\arch\\linux\\mem.c', 'file_copy\\psutil\\psutil\\arch\\linux\\mem.h', 'file_copy\\psutil\\psutil\\arch\\linux\\net.c', 'file_copy\\psutil\\psutil\\arch\\linux\\net.h', 'file_copy\\psutil\\psutil\\arch\\linux\\proc.c', 'file_copy\\psutil\\psutil\\arch\\linux\\proc.h', 'file_copy\\psutil\\psutil\\arch\\linux\\users.c', 'file_copy\\psutil\\psutil\\arch\\linux\\users.h', 'file_copy\\psutil\\psutil\\arch\\netbsd\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\netbsd\\cpu.h', 'file_copy\\psutil\\psutil\\arch\\netbsd\\disk.c', 'file_copy\\psutil\\psutil\\arch\\netbsd\\disk.h', 'file_copy\\psutil\\psutil\\arch\\netbsd\\mem.c', 'file_copy\\psutil\\psutil\\arch\\netbsd\\mem.h', 'file_copy\\psutil\\psutil\\arch\\netbsd\\proc.c', 'file_copy\\psutil\\psutil\\arch\\netbsd\\proc.h', 'file_copy\\psutil\\psutil\\arch\\netbsd\\socks.c', 'file_copy\\psutil\\psutil\\arch\\netbsd\\socks.h', 'file_copy\\psutil\\psutil\\arch\\openbsd\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\openbsd\\cpu.h', 'file_copy\\psutil\\psutil\\arch\\openbsd\\disk.c', 'file_copy\\psutil\\psutil\\arch\\openbsd\\disk.h', 'file_copy\\psutil\\psutil\\arch\\openbsd\\mem.c', 'file_copy\\psutil\\psutil\\arch\\openbsd\\mem.h', 'file_copy\\psutil\\psutil\\arch\\openbsd\\proc.c', 
     'file_copy\\psutil\\psutil\\arch\\openbsd\\proc.h', 'file_copy\\psutil\\psutil\\arch\\openbsd\\socks.c', 'file_copy\\psutil\\psutil\\arch\\openbsd\\socks.h', 'file_copy\\psutil\\psutil\\arch\\osx\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\osx\\cpu.h', 'file_copy\\psutil\\psutil\\arch\\osx\\disk.c', 'file_copy\\psutil\\psutil\\arch\\osx\\disk.h', 'file_copy\\psutil\\psutil\\arch\\osx\\mem.c', 'file_copy\\psutil\\psutil\\arch\\osx\\mem.h', 'file_copy\\psutil\\psutil\\arch\\osx\\net.c', 'file_copy\\psutil\\psutil\\arch\\osx\\net.h', 'file_copy\\psutil\\psutil\\arch\\osx\\proc.c', 'file_copy\\psutil\\psutil\\arch\\osx\\proc.h', 'file_copy\\psutil\\psutil\\arch\\osx\\sensors.c', 'file_copy\\psutil\\psutil\\arch\\osx\\sensors.h', 'file_copy\\psutil\\psutil\\arch\\osx\\sys.c', 'file_copy\\psutil\\psutil\\arch\\osx\\sys.h', 'file_copy\\psutil\\psutil\\arch\\solaris\\environ.c', 'file_copy\\psutil\\psutil\\arch\\solaris\\environ.h', 'file_copy\\psutil\\psutil\\arch\\windows\\cpu.c', 'file_copy\\psutil\\psutil\\arch\\windows\\cpu.h', 
     'file_copy\\psutil\\psutil\\arch\\windows\\disk.c', 'file_copy\\psutil\\psutil\\arch\\windows\\disk.h', 'file_copy\\psutil\\psutil\\arch\\windows\\mem.c', 'file_copy\\psutil\\psutil\\arch\\windows\\mem.h', 'file_copy\\psutil\\psutil\\arch\\windows\\net.c', 'file_copy\\psutil\\psutil\\arch\\windows\\net.h', 'file_copy\\psutil\\psutil\\arch\\windows\\ntextapi.h', 'file_copy\\psutil\\psutil\\arch\\windows\\proc.c', 
     'file_copy\\psutil\\psutil\\arch\\windows\\proc.h', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_handles.c', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_handles.h', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_info.c', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_info.h', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_utils.c', 'file_copy\\psutil\\psutil\\arch\\windows\\proc_utils.h', 'file_copy\\psutil\\psutil\\arch\\windows\\security.c', 'file_copy\\psutil\\psutil\\arch\\windows\\security.h', 'file_copy\\psutil\\psutil\\arch\\windows\\sensors.c', 'file_copy\\psutil\\psutil\\arch\\windows\\sensors.h', 
     'file_copy\\psutil\\psutil\\arch\\windows\\services.c', 'file_copy\\psutil\\psutil\\arch\\windows\\services.h', 'file_copy\\psutil\\psutil\\arch\\windows\\socks.c', 'file_copy\\psutil\\psutil\\arch\\windows\\socks.h', 'file_copy\\psutil\\psutil\\arch\\windows\\sys.c', 'file_copy\\psutil\\psutil\\arch\\windows\\sys.h', 'file_copy\\psutil\\psutil\\arch\\windows\\wmi.c', 'file_copy\\psutil\\psutil\\arch\\windows\\wmi.h', 'file_copy\\pycaw\\api\\audioclient\\__pycache__\\depend.cpython-39.pyc', 'file_copy\\pycaw\\api\\audioclient\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\pycaw\\api\\audiopolicy\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\pycaw\\api\\endpointvolume\\__pycache__\\depend.cpython-39.pyc', 'file_copy\\pycaw\\api\\endpointvolume\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend\\structures.py', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend\\__init__.py', 'file_copy\\pycaw\\api\\mmdeviceapi\\__pycache__\\__init__.cpython-39.pyc', 'file_copy\\psutil\\psutil\\arch\\solaris\\v10\\ifaddrs.c', 'file_copy\\psutil\\psutil\\arch\\solaris\\v10\\ifaddrs.h', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend\\__pycache__\\structures.cpython-39.pyc', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend\\__pycache__\\__init__.cpython-39.pyc']

List_Folder = ['script', 'setting', 'img', 'video', 'arduino', 'tools', 'txt', 'lib', 'file_copy', 'file_copy\\psutil', 'file_copy\\pycaw', 'file_copy\\psutil\\.github', 'file_copy\\psutil\\docs', 'file_copy\\psutil\\psutil', 'file_copy\\psutil\\scripts', 'file_copy\\pycaw\\api', 'file_copy\\pycaw\\__pycache__', 'file_copy\\psutil\\.github\\ISSUE_TEMPLATE', 'file_copy\\psutil\\.github\\workflows', 'file_copy\\psutil\\docs\\_static', 'file_copy\\psutil\\psutil\\arch', 'file_copy\\psutil\\psutil\\tests', 'file_copy\\psutil\\scripts\\internal', 'file_copy\\pycaw\\api\\audioclient', 'file_copy\\pycaw\\api\\audiopolicy', 'file_copy\\pycaw\\api\\endpointvolume', 'file_copy\\pycaw\\api\\mmdeviceapi', 'file_copy\\pycaw\\api\\__pycache__', 'file_copy\\psutil\\docs\\_static\\css', 'file_copy\\psutil\\psutil\\arch\\aix', 'file_copy\\psutil\\psutil\\arch\\bsd', 'file_copy\\psutil\\psutil\\arch\\freebsd', 'file_copy\\psutil\\psutil\\arch\\linux', 'file_copy\\psutil\\psutil\\arch\\netbsd', 'file_copy\\psutil\\psutil\\arch\\openbsd', 'file_copy\\psutil\\psutil\\arch\\osx', 'file_copy\\psutil\\psutil\\arch\\solaris', 'file_copy\\psutil\\psutil\\arch\\windows', 'file_copy\\pycaw\\api\\audioclient\\__pycache__', 'file_copy\\pycaw\\api\\audiopolicy\\__pycache__', 'file_copy\\pycaw\\api\\endpointvolume\\__pycache__', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend', 'file_copy\\pycaw\\api\\mmdeviceapi\\__pycache__', 'file_copy\\psutil\\psutil\\arch\\solaris\\v10', 'file_copy\\pycaw\\api\\mmdeviceapi\\depend\\__pycache__']

'''
Actual_List = os.listdir('file_copy')
for i in range(len(Actual_List)):
    Actual_List[i] = 'file_copy\\' + Actual_List[i]
Dir = True
while Dir == True:
    List_Dir = []
    for File in Actual_List:
        if os.path.isdir(File):
            List_Dir.append(File)
        else:
            List_File.append(File)
    if List_Dir == []:
        Dir = False
    else:
        Actual_List = []
        for Dir_Item in List_Dir:
            L = os.listdir(Dir_Item)
            for Item in L:
                Actual_List.append(Dir_Item + '\\' + Item)
            List_Folder.append(Dir_Item)'''

def SAVE():
    print('__________________________Start Save__________________________')
    Dico = {}
    for Item in List_File:
        with open(Item,'rb') as file:
            Dico[Item] = base64.b64encode(file.read()).decode('utf-8')
    Encode_Dico = base64.b64encode(lzma.compress(bytes(str(Dico), 'utf-8'))).decode('utf-8')
    with open('txt\\Script_Save.txt','w',encoding='utf-8') as script:
        script.write(Encode_Dico)
    print('__________________________End Save__________________________')

def GET_SAVE(Name_Script):
    print('__________________________Start Récuperation__________________________')
    print(f'__________________________{Name_Script}__________________________')
    with open('txt\\Script_Save.txt','r',encoding='utf-8') as script:
        Dico = ast.literal_eval(lzma.decompress(base64.b64decode(script.read())).decode('utf-8'))
    if Name_Script in list(Dico.keys()):
        with open(Name_Script,'wb') as script:
            script.write(base64.b64decode(Dico[Name_Script]))
    else:
        print(f"{Name_Script} n'a pas été trouvé dans la sauvegarde.")
    print('__________________________End Récuperation__________________________')

for Item in List_Folder:
    if not os.path.isdir(Item):
        os.makedirs(Item)
for Item in List_File:
    if not os.path.isfile(Item):
        GET_SAVE(Item)

if __Devellopement__:
    from tools.Pip import *

def DECODE(Char,Cle):
    for j in range(len(Cle)):
        List = Cle[-(1+j)]
        Join_Char = ''
        for Sous_Char in Char:
            if not Sous_Char in Join_Char:
                Join_Char += Sous_Char
        List_Char_Base = Join_Char
        List_Emplacement = {}
        for j in range(len(List)):
            Sous_List = []
            for i in range(len(Char)):
                if Char[i] == List_Char_Base[j]:
                    Sous_List.append(i)
            List_Emplacement[List[j]] = Sous_List
        for Key in list(List_Emplacement.keys()):
            for i in range(len(List_Emplacement[Key])):
                Char = Char[:List_Emplacement[Key][i]] + Key + Char[List_Emplacement[Key][i]+1:]
    return Char

def GET_KEY():
    with open('txt\\Key.txt','r') as f:
        Cle = list(f.readlines())
    for i in range(len(Cle)):
        Cle[i] = Cle[i].replace('\n','')
    return Cle

def GET_CHAR():
    with open('txt\\Key_Encode.txt','r') as f:
        Ligne = f.read()
    Char = lzma.decompress(base64.b64decode(Ligne)).decode('utf-8')
    return Char

import keyboard as kb
import tkinter as tk
import tools.Tools as tl
import Redirect as re
import Arduino as ar
import Class as cl
from customtkinter import *
from tools.langages import *
from random import *
from time import *
from copy import *
if not __Devellopement__:
    from moviepy.editor import AudioFileClip
    from lib.TkVideoPlayer import TkinterVideo as TkV
import threading
import requests
import sys

if not os.path.isfile(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt')):
    with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
        pass

def DEV_FRAME():
    global __Develloper__
    if __Develloper__:
        def DEV():
            Fenetre = CTk(fg_color='#222222')
            Fenetre.title("")
            Fenetre.iconbitmap(default=tl.GET_ABSOLUTE_PATH("img\\Magic_3_-removebg-preview.ico"))
            Fenetre.resizable(width=False,height=False)
            with open('txt\\Dev_Parametre.txt', 'r') as file:
                Dico = eval(file.read())
            
            def SAVE():
                global Ratio
                global Loading_Card
                global Boutton_Factice_List
                global Fast_Open_Fenetre

                try:
                    Loading_Card = Loading_Pin.get()
                except:
                    print("Entrée invalide 1")

                try:
                    Fast_Open_Fenetre = Fast_Open.get()
                    if Fast_Open_Fenetre == "三 Fast Open...":
                        Fast_Open_Fenetre = None
                    else:
                        Fast_Open_Fenetre = '\'' + Fast_Open_Fenetre + '\''
                except:
                    print("Entrée invalide 2")

                try:
                    if Boutton_Factice.get() != '':
                        Boutton_Factice_List = eval('[\'f'+Boutton_Factice.get().replace(',','\',\'f')+'\']')
                    else:
                        Boutton_Factice_List = []
                except:
                    print("Entrée invalide 3")

                try:
                    if Ratio_Force.get() == 'None':
                        Ratio_Write = None
                    elif float(Ratio_Force.get()) >= 0:
                        Ratio = float(Ratio_Force.get())
                        Ratio_Write = Ratio
                except:
                    print("Entrée invalide 4")
                
                cl.Boutton_Factice_List = Boutton_Factice_List
                with open('txt\\Dev_Parametre.txt', 'w') as file:
                    file.write('{\'Pin_Loading\':' + f'{Loading_Card}' + ',\'Fast_Open\':' +  f'{Fast_Open_Fenetre}' + ',\'Boutton_Factice\':' +  f'{Boutton_Factice_List}' + ',\'Ratio_Force\':' +  f'{Ratio_Write}' + '}')
            
            CTkLabel(Fenetre, text="Card Loading", text_color='white').pack(side=TOP, padx=10, pady=2.5)
            Short_List_Var = StringVar()
            OptionList = ['True','False']
            Loading_Pin = CTkOptionMenu(Fenetre,hover=False,fg_color='#222222',button_color='#222222',values=OptionList,corner_radius=10,dynamic_resizing=True,variable=Short_List_Var)
            if Dico['Pin_Loading']:
                Loading_Pin.set('True')
            else:
                Loading_Pin.set('False')
            Loading_Pin.pack(side=TOP, padx=10, pady=2.5)

            CTkLabel(Fenetre, text="Fast Open", text_color='white').pack(side=TOP, padx=10, pady=2.5)
            Short_List_Var = StringVar()
            OptionList = ['三 Fast Open...','Script Editor','Parameter Manager','Save Parameter','Manual Card Connection','Card Programme Upload']
            Fast_Open = CTkOptionMenu(Fenetre,hover=False,fg_color='#222222',button_color='#222222',values=OptionList,corner_radius=10,dynamic_resizing=True,variable=Short_List_Var)
            if Dico['Fast_Open'] == None:
                Fast_Open.set("三 Fast Open...")
            else:
                Fast_Open.set(Dico['Fast_Open'])
            Fast_Open.pack(side=TOP, padx=10, pady=2.5)

            CTkLabel(Fenetre, text="Boutton Factice (A1,2,7...)", text_color='white').pack(side=TOP, padx=10, pady=2.5)
            Boutton_Factice = CTkEntry(Fenetre)
            Boutton_Factice.insert(0, str(Dico['Boutton_Factice']).replace('[\'f','').replace('\']','').replace('\', \'f',',').replace('[]',''))
            Boutton_Factice.pack(side=TOP, padx=10, pady=2.5)

            CTkLabel(Fenetre, text="Ratio Forcé ]0;+∞[", text_color='white').pack(side=TOP, padx=10, pady=2.5)
            Ratio_Force = CTkEntry(Fenetre)
            Ratio_Force.insert(0, str(Dico['Ratio_Force']))
            Ratio_Force.pack(side=TOP, padx=10, pady=2.5)

            CTkButton(Fenetre, text="Save", command=SAVE).pack(side=TOP, padx=10, pady=5)
            
            Fenetre.mainloop()
    
        Dev = threading.Thread(target=DEV)
        Dev.start()

def ADD_HOTKEY():
    kb.add_hotkey('f12', DEV_FRAME, suppress=True, trigger_on_release=True)

def VERIF():
    global __Develloper__
    if lzma.decompress(base64.b64decode(__Key__)).decode('utf-8') == DECODE(GET_CHAR(),GET_KEY()):
        __Develloper__ = True
        ADD_HOTKEY()
Verif = threading.Thread(target=VERIF)
Verif.start()

try:
    response = requests.get("https://api.ipify.org")
    response.raise_for_status()  # Vérifier si la requête a réussi
    public_ip = response.text
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la récupération de l'adresse IP publique : {e}")
    public_ip = None

FalashBang = False
if public_ip != '109.215.91.30' and public_ip != '82.126.186.61' and public_ip != '37.72.217.55' and randint(1,25) == 25:
    FalashBang = True
Pin_Frame_Numerique = []
Pin_Frame_Analogique = []
Pin_Parametre_Instance = []
Dechifrage_Ligne = None
Reboot = False
Update_Etat = False

Widht ,Height = tl.GET_SCREEN_DIMENSION()
Fenetre_widht, Fenetre_Height = 0, 0
Fenetre_widht_Ratio, Fenetre_Height_Ratio = 1, 1
Last_Fenetre_widht_Ratio, Last_Fenetre_Height_Ratio = -1, -1
List_Frame_Resize = []

Ratio = Height/1080
Ratio_Percent = (Ratio-480/1080)*1/(1-(480/1080))

with open('txt\\Dev_Parametre.txt', 'r') as file:
    Dico = eval(file.read())

Boutton_Factice_List = Dico['Boutton_Factice']
Fast_Open_Fenetre = Dico['Fast_Open']
Loading_Card = Dico['Pin_Loading']
if Dico['Ratio_Force'] != None:
    Ratio = Dico['Ratio_Force']
    Ratio_Percent = (Ratio-480/1080)*1/(1-(480/1080))

def MAIN(Port_Serie,Port_De_La_Carte):

    global Loading_Card
    global Fast_Open_Fenetre
    global Widht, Height
    global Fenetre_widht, Fenetre_Height
    global List_Frame_Resize

    def ON_RESIZE(event):
        global Fenetre_widht_Ratio, Fenetre_Height_Ratio
        global Last_Fenetre_widht_Ratio, Last_Fenetre_Height_Ratio
        Fenetre_widht_Ratio, Fenetre_Height_Ratio = tl.GET_ACTUAL_FENETRE_WIDHT_HEIGHT_RATIO(Fenetre,Fenetre_widht,Fenetre_Height)
        if Last_Fenetre_widht_Ratio != Fenetre_widht_Ratio or Last_Fenetre_Height_Ratio != Fenetre_Height_Ratio:
            Last_Fenetre_widht_Ratio, Last_Fenetre_Height_Ratio = Fenetre_widht_Ratio, Fenetre_Height_Ratio
            #if Frame_Manage_Preset.Open:
            #    Frame_Manage_Preset.RESIZE(Fenetre_widht_Ratio, Fenetre_Height_Ratio)
            print(len(List_Frame_Resize))
            for Item in List_Frame_Resize:
                if Item.Open:
                   Item.RESIZE(Fenetre_widht_Ratio, Fenetre_Height_Ratio)

    #Creation de la fentre principale
    Fenetre = CTk(fg_color='#222222')
    Fenetre.title("")
    Fenetre.iconbitmap(default=tl.GET_ABSOLUTE_PATH("img\\Magic_3_-removebg-preview.ico"))
    H = 825
    L = 1250
    Fenetre.geometry(f"{round(L*Ratio)}x{round(H*Ratio)}+{round(50*Ratio)}+{round(25*Ratio)}")
    Fenetre.minsize(width=0,height=0)
    Fenetre.maxsize(width=Widht,height=Height-70)
    #Fenetre.resizable(width=False,height=False)
    Fenetre.bind("<Configure>", ON_RESIZE)

    Fenetre_widht, Fenetre_Height = L*Ratio, H*Ratio

    #Definition des variables pour parametre les dimension des button, du texte
    Height_Button = 40
    Width_Button = 250
    Txt_Size = round(25*Ratio)
    Police = 'Arial'
    Script_Editor_Open = False #Definition de la variable de l'etat du script editor

    #Creation de la frame qui contient les buttons utile
    Tab = CTkFrame(Fenetre,fg_color='#2D2D2D',corner_radius=10)
    Tab.place(x=(L-(Width_Button*(4.1-0.1*Ratio_Percent)+7.5*4+15*10))*0.45*Ratio,y=H*0.025*Ratio)
    H_Befor = (H*0.025*2+Height_Button+7.5*2)*Ratio
    
    #Creation des instance des button principale
    Frame_Script_Editor = cl.Script_Editor(Fenetre, 'None', H*Ratio/1.25, L*Ratio/1.25)
    Frame_Save_Preset = cl.Save_Preset(Fenetre, H*Ratio, L*Ratio)
    Frame_Manage_Preset = None
    Frame_Card_Manual = cl.Card_Manual(Fenetre, H*Ratio, L*Ratio)
    Frame_Card_Type = cl.Card_Type(Fenetre, H*Ratio, L*Ratio)
    Error_Instance = cl.Error(Fenetre, H*Ratio, L*Ratio)
    Operation_Is_Running_Instance = cl.Operation_Is_Running(Fenetre, H, L)
    #List_Frame_Resize.append(Frame_Script_Editor)
    List_Frame_Resize.append(Frame_Save_Preset)
    #List_Frame_Resize.append(Frame_Card_Manual)
    #List_Frame_Resize.append(Frame_Card_Type)
    List_Frame_Resize.append(Error_Instance)
    List_Frame_Resize.append(Operation_Is_Running_Instance)

    def SAVE_PRESET(): #Fonction du button Save Parametre
        nonlocal Frame_Manage_Preset
        if not Frame_Save_Preset.Open:
            Frame_Save_Preset.CREATE_FRAME() #Crée la frame pour save les parametre
            if Frame_Manage_Preset == None:
                Frame_Manage_Preset = cl.Manage_Preset(Fenetre,H*Ratio/1.25,L*Ratio/1.25, [])
                List_Frame_Resize.append(Frame_Manage_Preset)
            if Frame_Manage_Preset.Open:
                def WAIT():
                    while not Frame_Save_Preset.Open:
                        sleep(0.1)
                    while Frame_Save_Preset.Open:
                        sleep(0.1)
                    Frame_Manage_Preset.CREATE_FRAME(None,Frame_Save_Preset.Name)
                Wait = threading.Thread(target=WAIT) 
                Wait.start()

    def IMPORT_PRESET(): #Fonction du button Manage Parametre
        nonlocal Frame_Manage_Preset
        if Frame_Manage_Preset == None:
            portserie.traitementInitialisation()
            Frame_Manage_Preset = cl.Manage_Preset(Fenetre,H*Ratio/1.25,L*Ratio/1.25, [])
            List_Frame_Resize.append(Frame_Manage_Preset)
        if not Frame_Manage_Preset.Open:
            Tempo = deepcopy(portserie.identifiantsPinsAnalogiques)
            for Item in portserie.identifiantsPinsNumeriques:
                Tempo.append(str(Item))
            Frame_Manage_Preset.CREATE_FRAME(Tempo,False) #Crée la frame pour manager les parametre

    def UPDATE_CARTE(): #Fonction du button update de la carte
        global Pin_Frame_Numerique
        global Pin_Frame_Analogique
        global Pin_Parametre_Instance
        global Boutton_Factice_List
        global Update_Etat
        nonlocal Port_De_La_Carte
        if not Update_Etat:
            Update_Etat = True
            for Item in Pin_Frame_Numerique:
                Item.Frame.destroy()
                del Item
            for Item in Pin_Frame_Analogique:
                Item.Frame.destroy()
                del Item
            for Item in Pin_Parametre_Instance:
                if Item.Frame_Choice != None:
                    Item.Frame_Choice.destroy()
                if Item.Close_Button != None:
                    Item.Close_Button.destroy()
                del Item
            def WAIT(): #Attendre que la nouvelle carte soit active
                global portDeLaCarte
                while not Port_Serie.Alive:
                    sleep(0.1)
                PIN_FRAME_CREATION(int(portserie.nombresDePinsNumeriques),int(portserie.nombresDePinsAnalogiques),portserie.identifiantsPinsNumeriques,portserie.identifiantsPinsAnalogiques) #Creation des nouveaux pin
                portDeLaCarte = Port_De_La_Carte
            Wait = threading.Thread(target=WAIT)
            if not Port_Serie.Alive and (Port_De_La_Carte != None or not Port_De_La_Carte): #Si la carte n'est pas brancher
                if Frame_Card_Manual.Port_Selec != 'Auto' and Frame_Card_Manual.Port_Selec != None:
                    Port_De_La_Carte = Frame_Card_Manual.Port_Selec
                else:
                    Port_De_La_Carte = carte.port(0)
                if Port_De_La_Carte:                        
                    Config_Return = portserie.configuration(Port_De_La_Carte)
                    if Config_Return == True:
                        if portserie.initialisation == False: 
                            Return = portserie.traitementInitialisation()
                            if Return == -1:
                                Error_Instance.POP_UP('You Should\nProbably Upload\nThe Programme') #Pop up d'erreur
                                portserie.ser.close()
                            elif not Return:
                                Error_Instance.POP_UP('Card unplug\nduring the\ninitialisation') #Pop up d'erreur
                        Wait.start()
                    else:
                        Port_De_La_Carte = None
                        Error_Instance.POP_UP('Port Invalid') #Pop up d'erreur)
                elif not portDeLaCarte and Boutton_Factice_List != []:
                    PIN_FRAME_CREATION(0,0,[],[])   
                else:
                    Error_Instance.POP_UP(Phrase_Aucune_Carte_Brancher_Une_Carte_Valide) #Pop up d'erreur
                Update_Etat = False
            elif Port_Serie.Alive: #Si la carte est bien active
                #Detruit la carte actuel et les frame des pins
                Port_Serie.KILL()
                Dechifrage_Ligne.Setup = True
                Wait.start()
                Port_De_La_Carte = carte.port(0)
                Update_Etat = False
                UPDATE_CARTE()

    def CARD_MANUAL():
        Frame_Card_Manual.CREATE_FRAME()
        def WAIT():
            while not Frame_Card_Manual.Open:
                sleep(0.1)
            while Frame_Card_Manual.Open:
                sleep(0.1)
            if Frame_Card_Manual.Close_By == 1:
                Frame_Card_Manual.Close_By = 0
                Stop_Event = threading.Event()
                def loading():
                    Operation_Is_Running_Instance.CREATE_FRAME()
                    while not Stop_Event.is_set():
                        sleep(0.1)
                    Operation_Is_Running_Instance.DESTROY_FRAME()
                Loading = threading.Thread(target=loading)
                Loading.start()
                UPDATE_CARTE()
                Stop_Event.set()  
        Wait = threading.Thread(target=WAIT)
        Wait.start()
    
    def CARD_TYPE():
        Frame_Card_Type.CREATE_FRAME()
        def WAIT():
            while not Frame_Card_Type.Open:
                sleep(0.1)
            while Frame_Card_Type.Open:
                sleep(0.1)
            if Frame_Card_Type.Close_By == 1:
                Frame_Card_Type.Close_By = 0
                if Frame_Card_Manual.Port_Selec != 'Auto' and Frame_Card_Manual.Port_Selec != None:
                    Port_De_La_Carte = Frame_Card_Manual.Port_Selec
                else:
                    Port_De_La_Carte = carte.port(0)
                if Port_De_La_Carte != None:
                    try:
                        portserie.ser.close()
                    except:
                        pass
                    Stop_Event = threading.Event()
                    def loading():
                        Operation_Is_Running_Instance.CREATE_FRAME()
                        while not Stop_Event.is_set():
                            sleep(0.1)
                        Operation_Is_Running_Instance.DESTROY_FRAME()
                    Loading = threading.Thread(target=loading)
                    Loading.start()
                    Return = ar.UPLOAD(Port_De_La_Carte,Frame_Card_Type.Type_Carte)
                    if Return == 1:
                        Error_Instance.POP_UP('The Programme\nHas Been\nSuccefuly Upload')
                        UPDATE_CARTE()
                    elif Return == 0:
                        Error_Instance.POP_UP('Please Select\nA Valid\nType Of Card')
                    Stop_Event.set()
                else:
                    Error_Instance.POP_UP('Please Select\nA Port For\nThe Card')
                
        Wait = threading.Thread(target=WAIT)
        Wait.start()

    def SCRIPT_EDITOR(): #Fonction du button permettant d'ouvrir le script editor

        def CLOSE(Frame_Script_Editor,Close_Button): #Fonction pour fermer le script editor

            def CLOSE_CONFIRMATION(Item): #Fonction pour fermer le script editor apres validation ou sauvegarde deja effectuer, destruction des item du scipt editor
                nonlocal Script_Editor_Open
                if Item != 'None':
                    Item.destroy()
                if Frame_Script_Editor.Frame:
                    Frame_Script_Editor.Frame.destroy()
                if Frame_Script_Editor.Save_Button:
                    Frame_Script_Editor.Save_Button.destroy()
                if Frame_Script_Editor.Frame_Choice:
                    Frame_Script_Editor.Frame_Choice.destroy()
                Close_Button.destroy()
                Frame_Script_Editor.Name = 'None'
                if os.path.isfile(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt')):
                    os.remove(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'))
                Script_Editor_Open = False
            
            def CLOSE_ANNULATION(Item): #Fonction annuler la fermeture du script editor
                Item.destroy()
            
            if Frame_Script_Editor.Name == 'None': #Si le script editor est dans la phase d'ouverture / choix du fichier
                CLOSE_CONFIRMATION('None')
            else: 
                #Obtention des ligne des deux script editer et destination
                try:
                    with open(f'script\\{Frame_Script_Editor.Name}.txt', 'r') as fichier_1:
                        Ligne_1 = fichier_1.readlines()
                except:
                    Ligne_1 = None
                Ligne_2 = None
                if os.path.isfile(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt')):
                    with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'r') as fichier_0:
                        Ligne = fichier_0.readlines()
                    with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'w') as fichier:
                        Ligne_2 = []
                        Item_Pop = Ligne.pop(0)
                        for i in range(len(Ligne)):
                            Item = eval(Ligne[i])
                            List = Frame_Script_Editor.Script_Line_List[i]
                            if len(List) > 1:
                                for i in range(1,len(List)-1):
                                    Sous_Item = List[i+1]
                                    if Item['_'][i-1] == 'Text_Box':
                                        try:
                                            Item['Parametre'][i-1] = Sous_Item.get("0.0", "end")[:-1]
                                        except:
                                            Item['Parametre'][i-1] = None
                                    elif 'Menu' in Item['_'][i-1]:
                                        if not '三' in Sous_Item.get():
                                            Item['Parametre'][i-1] = Sous_Item.get()
                                        else:
                                            Item['Parametre'][i-1] = None
                                    elif Item['_'][i-1] == 'Boutton':
                                        if not 'Select Touch' in Sous_Item.cget("text") and not 'Press a Touch' in Sous_Item.cget("text"):
                                            Item['Parametre'][i-1] = Sous_Item.cget("text")
                                        else:
                                            Item['Parametre'][i-1] = None
                            Ligne_2.append(str(Item)+'\n')
                        Ligne_2.insert(0,Item_Pop)
                        fichier.writelines(Ligne_2)
                        
                if Ligne_1 != Ligne_2: #Si le fichier n'a deja ete sauvegarder, creation de la fenetre de choix
                    self_L = L*Ratio/1.25
                    self_H = H*Ratio/1.25
                    Frame_Choice = CTkFrame(Fenetre,fg_color='black',border_color='White',border_width=2*Ratio,width=self_L,height=self_H,corner_radius=5)
                    Frame_Choice.place(x=((self_L*1.25)-self_L)/2,y=((self_H*1.25)-self_H)/2)
                    Txt = CTkLabel(Frame_Choice,fg_color='transparent',text=Phrase_Etes_Vous_Sur_De_Vouloir_Fermer_Sans_Sauvegarder,text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,round(30)*Ratio))
                    Txt.place(x=self_L/2-75*Ratio/2-275*Ratio,y=self_H/2-75*Ratio/2-75*Ratio)
                    Yes = CTkButton(Frame_Choice,fg_color='#2F64B4',text=Phrase_Oui,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CLOSE_CONFIRMATION(Frame_Choice))
                    Yes.place(x=self_L/2-75*Ratio/2-75*Ratio,y=self_H/2-75*Ratio/2)
                    No = CTkButton(Frame_Choice,fg_color='#2F64B4',text=Phrase_Non,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CLOSE_ANNULATION(Frame_Choice))
                    No.place(x=self_L/2-75*Ratio/2+75*Ratio,y=self_H/2-75*Ratio/2)
                else: #Si le fichier a deja ete sauvegarder
                    CLOSE_CONFIRMATION('None')
                
        nonlocal Script_Editor_Open
        if not Script_Editor_Open: #Ouverture du script editor si il n'est pas deja ouvert
            Script_Editor_Open = True
            Frame_Script_Editor.CREATE_FRAME_CHOICE()
            self_L = L*Ratio/1.25
            self_H = H*Ratio/1.25
            Close_Button = CTkButton(Fenetre,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,Txt_Size-(5-5*Ratio_Percent)),command=lambda:CLOSE(Frame_Script_Editor,Close_Button))
            Close_Button.place(x=((self_L*1.25)-self_L)/2-32.5*Ratio+self_L,y=((self_H*1.25)-self_H)/2-35*Ratio)

    def UPDATE_CARTE_BIS():
        Stop_Event = threading.Event()
        def loading():
            Operation_Is_Running_Instance.CREATE_FRAME()
            while not Stop_Event.is_set():
                sleep(0.1)
            Operation_Is_Running_Instance.DESTROY_FRAME()
        Loading = threading.Thread(target=loading)
        Loading.start()
        UPDATE_CARTE()
        Stop_Event.set()
        
    #Creation du button permettant de sauvegarder les parametre
    Save_Preset = CTkButton(Tab,fg_color='#2F64B4',text=Phrase_Sauvegarder_Les_Parametres,height=Height_Button*Ratio,width=Width_Button*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SAVE_PRESET)
    Save_Preset.grid(column=0,row=0,padx=15*Ratio,pady=7.5*Ratio)
    #Creation du button permettant d'importer des parametre sauvegarder
    Import_Preset = CTkButton(Tab,fg_color='#2F64B4',text=Phrase_Gerer_Les_Parametres,height=Height_Button*Ratio,width=Width_Button*Ratio,corner_radius=10,font=(Police,Txt_Size),command=IMPORT_PRESET)
    Import_Preset.grid(column=1,row=0,padx=15*Ratio,pady=7.5*Ratio)
    #Creation du button permettant d'ouvrir le script editor
    Scrip_Editor = CTkButton(Tab,fg_color='#2F64B4',text=Phrase_Editeur_De_Scripts,height=Height_Button*Ratio,width=Width_Button*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SCRIPT_EDITOR)
    Scrip_Editor.grid(column=3,row=0,padx=15*Ratio,pady=7.5*Ratio)
    #Creation du button permettant de mettre a jour les pin connecter
    Update_Pin_Connection = CTkButton(Tab,fg_color='#2F64B4',text=Phrase_Actualiser_La_Carte,height=Height_Button*Ratio,width=Width_Button*Ratio,corner_radius=10,font=(Police,Txt_Size),command=UPDATE_CARTE_BIS)
    Update_Pin_Connection.grid(column=4,row=0,padx=15*Ratio,pady=7.5*Ratio)
    
    def SHORT(Choice): #Fonction du menu deroulant pour trier les pin par l'ordre choisi
        if Choice == f"{Phrase_Trier_Par} {Phrase_Numeros}":
            Short_List.set(f"三 {Phrase_Trier_Par} {Phrase_Numeros}")
            update_frame_position(None)
            Global_Pin_Frame = Pin_Frame_Numerique + Pin_Frame_Analogique
            Order = []
            for Item in Global_Pin_Frame:
                if Order == []:
                    Order = [Item]
                else:
                    i = 0
                    while i < len(Order) and int(str(Order[i].Id).replace('A','').replace('f','')) < int(str(Item.Id).replace('A','').replace('f','')):
                        i += 1
                    Order.insert(i,Item)
            x = 0
            y = 0
            for i in range(len(Order)):
                Order[i].Frame.grid(column=x,row=y)
                x += 1
                if x >= 5:
                    x = 0
                    y += 1
        elif Choice == f"{Phrase_Trier_Par} {Phrase_Type} {Phrase_Bouton}/{Phrase_Potentiometre}":
            Short_List.set(f"三 {Phrase_Trier_Par} {Phrase_Type} {Phrase_Bouton}/{Phrase_Potentiometre}")
            update_frame_position(None)
            x = 0
            y = 0
            for Item in Pin_Frame_Numerique:
                Item.Frame.grid(column=x,row=y)
                x += 1
                if x >= 5:
                    x = 0
                    y += 1
            for Item in Pin_Frame_Analogique:
                Item.Frame.grid(column=x,row=y)
                x += 1
                if x >= 5:
                    x = 0
                    y += 1
        elif Choice == f"{Phrase_Trier_Par} {Phrase_Type} {Phrase_Potentiometre}/{Phrase_Bouton}":
            Short_List.set(f"三 {Phrase_Trier_Par} {Phrase_Type} {Phrase_Potentiometre}/{Phrase_Bouton}")
            update_frame_position(None)
            x = 0
            y = 0
            for Item in Pin_Frame_Analogique:
                Item.Frame.grid(column=x,row=y)
                x += 1
                if x >= 5:
                    x = 0
                    y += 1
            for Item in Pin_Frame_Numerique:
                Item.Frame.grid(column=x,row=y)
                x += 1
                if x >= 5:
                    x = 0
                    y += 1
    
    # Création du menu déroulant
    Short_List_Var = StringVar()
    OptionList = [f"{Phrase_Trier_Par} {Phrase_Numeros}", f"{Phrase_Trier_Par} {Phrase_Type} {Phrase_Bouton}/{Phrase_Potentiometre}", f"{Phrase_Trier_Par} {Phrase_Type} {Phrase_Potentiometre}/{Phrase_Bouton}"]
    Short_List = CTkOptionMenu(Fenetre,hover=False,fg_color='#222222',button_color='#222222',values=OptionList,height=Height_Button*Ratio,width=Width_Button*Ratio,corner_radius=10,font=(Police,Txt_Size),dynamic_resizing=True,command=SHORT,variable=Short_List_Var)
    Short_List.set(f"三 {Phrase_Trier_Par} ...")
    Short_List.place(x=(L-(Width_Button*4.25+7.5*4))*0.5*Ratio,y=H_Befor)
    
    # Création de la frame pour cacher la flèche du menu déroulant
    Space_Tab = CTkFrame(Fenetre,height=50*Ratio,width=50*Ratio,fg_color="#222222")
    H_Befor_Bis = H_Befor
    Space_Tab.place(x=(L-(Width_Button*(3.7+0.05*Ratio_Percent)+7.5*4))*Ratio,y=H_Befor_Bis)
    
    # Mise à jour de la position de la frame lorsque la taille du menu déroulant change
    def update_frame_position(event):
        x_position = Short_List.winfo_x() + Short_List.winfo_width() - Space_Tab.winfo_width() + 8  # Décalage de 8 pixels vers la droite
        Space_Tab.place(x=x_position, y=H_Befor_Bis)
    
    Short_List.bind("<Configure>", update_frame_position)
    
    H_Befor += (H*0.025+Height_Button)*Ratio

    #Creation de la frame d'emplacement des pin numerique et analogique
    PinFrame = CTkScrollableFrame(Fenetre,fg_color='#2D2D2D',width=1100*Ratio,height=(580+20*Ratio_Percent)*Ratio)
    PinFrame.place(x=(L-(Width_Button*(4.45-0.1*Ratio_Percent)+7.5*4))*0.5*Ratio,y=H_Befor)
    #Creation du boutton permettant de mettre a la main le port de la carte
    Card_Manual = CTkButton(Fenetre,fg_color='#741010',hover_color='#550E0E',border_color='black',border_width=2*Ratio,text=Phrase_Port_Manuel_De_La_Carte,height=25*Ratio,width=25*Ratio,corner_radius=10,font=(Police,Txt_Size),command=CARD_MANUAL)
    #Card_Manual.pack(side='right', anchor='s', padx=10, pady=10)
    Card_Manual.place(x=(L-315)*Ratio,y=(H-45)*Ratio)
    #Creation du boutton permettant de mettre le type de carte
    Card_Type= CTkButton(Fenetre,fg_color='#741010',hover_color='#550E0E',border_color='black',border_width=2*Ratio,text=Phrase_Téléverser_Le_Code_Sur_La_Carte,height=25*Ratio,width=25*Ratio,corner_radius=10,font=(Police,Txt_Size),command=CARD_TYPE)
    #Card_Type.pack(side='right', anchor='s', padx=10, pady=10)
    Card_Type.place(x=(L-700)*Ratio,y=(H-45)*Ratio)

    #Creation du txt d'alerte
    #Card_Type= CTkLabel(Fenetre,bg_color='transparent',text_color='red',text='If something don\'t work there some chance that\nyour port is already connected to another thing',height=25*Ratio,width=25*Ratio,corner_radius=10,font=(Police,Txt_Size))
    #Card_Type.place(x=(L-1225)*Ratio,y=(H-55)*Ratio)

    #Definition des variables des pin numerique et analogique
    Running = False

    def PIN_FRAME_CREATION(Nombre_Numerique,Nombre_Analogique,Id_Numerique,Id_Analogique): #Creation des frame des pin
        global Pin_Frame_Numerique
        global List_Frame_Resize
        global Pin_Frame_Analogique
        global Pin_Parametre_Instance
        global Boutton_Factice_List
        nonlocal Frame_Manage_Preset
        nonlocal Running

        if not Running:
            Running = True
            for Item in Boutton_Factice_List:
                if 'A' in Item:
                    Nombre_Analogique += 1
                    Id_Analogique.append(Item)
                else:
                    Nombre_Numerique += 1
                    Id_Numerique.append(Item)
            
            for i in range(len(Pin_Frame_Numerique)):
                Item = Pin_Frame_Numerique.pop(0)
                List_Frame_Resize.pop(List_Frame_Resize.index(Item))
                del Item
            for i in range(len(Pin_Frame_Analogique)):
                Item = Pin_Frame_Analogique.pop(0)
                List_Frame_Resize.pop(List_Frame_Resize.index(Item))
                del Item
            for i in range(len(Pin_Parametre_Instance)):
                Item = Pin_Parametre_Instance.pop(0)
                List_Frame_Resize.pop(List_Frame_Resize.index(Item))
                del Item

            Pin_Frame_Numerique = []
            Pin_Frame_Analogique = []
            Pin_Parametre_Instance = []
            x = 0
            y = 0
            Tempo = deepcopy(Id_Analogique)
            for Item in Id_Numerique:
                Tempo.append(str(Item))
            if Frame_Manage_Preset == None:
                Frame_Manage_Preset = cl.Manage_Preset(Fenetre,H*Ratio/1.25,L*Ratio/1.25, Tempo)
                List_Frame_Resize.append(Frame_Manage_Preset)
            #Ecrit les modification a faire dans le setting actuel si nouveau pin ou pin en moins
            if not os.path.isfile(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt')):
                with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
                    pass
            with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                Ligne = fichier.readlines()
            with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
                for Item in Ligne:
                    if Item.split(':')[1] in Tempo:
                        fichier.write(Item)
                        Tempo.pop(Tempo.index(Item.split(':')[1]))
                for Item in Tempo:
                    if 'A' in Item:
                        fichier.write(f'A:{Item}:None\n')
                    else:
                        fichier.write(f'N:{Item}:None\n')
            with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                for i in range(Nombre_Numerique+Nombre_Analogique):
                    if i < Nombre_Numerique:
                        Parametre = cl.Pin_Parametre(Fenetre,Id_Numerique[i],H*Ratio,L*Ratio) #Creation d'une instance pour les parametre du pin
                        Frame = cl.Frame_Bp(PinFrame,i,x,y,250*Ratio,200*Ratio,i+1,Parametre,Id_Numerique[i]) #Creation d'une instance boutton poussoir
                        Frame.CREATE_FRAME()
                        Pin_Frame_Numerique.append(Frame)
                    else:
                        Parametre = cl.Pin_Parametre(Fenetre,Id_Analogique[i-Nombre_Numerique],H*Ratio,L*Ratio) #Creation d'une instance pour les parametre du pin
                        Frame = cl.Frame_Potence(PinFrame,i,x,y,250*Ratio,200*Ratio,i+1-Nombre_Numerique,Parametre,Id_Analogique[i-Nombre_Numerique]) #Creation d'une instance potentiometre
                        Frame.CREATE_FRAME()
                        Pin_Frame_Analogique.append(Frame)
                    List_Frame_Resize.append(Parametre)
                    List_Frame_Resize.append(Frame)
                    Pin_Parametre_Instance.append(Parametre)
                    x += 1
                    if x >= 5: #Nombre de pin par ligne
                        x = 0
                        y += 1
            SHORT(Short_List.get().replace('三 ',''))
            Running = False

    if not __Devellopement__:
        Videoplayer = TkV(master=Fenetre, scaled=True)
        if FalashBang:
            Videoplayer.load(tl.GET_ABSOLUTE_PATH("video\\Flash Bang Easter.mp4"))
        else:
            Videoplayer.load(tl.GET_ABSOLUTE_PATH("video\\Logo.mp4"))
        Videoplayer.pack(expand=True, fill="both")
        Videoplayer.play()
        def WAIT():
            sleep(6)
            if Fenetre:
                Videoplayer.stop()
                Videoplayer.destroy()
                Stop_Event = threading.Event()
                def loading():
                    Operation_Is_Running_Instance.CREATE_FRAME()
                    while not Stop_Event.is_set():
                        sleep(0.1)
                    Operation_Is_Running_Instance.DESTROY_FRAME()
                Loading = threading.Thread(target=loading)
                Loading.start()
                if Loading_Card:
                    UPDATE_CARTE()
                elif Boutton_Factice_List != []:
                    PIN_FRAME_CREATION(0,0,[],[])
                Stop_Event.set()
        Wait = threading.Thread(target=WAIT)
        Wait.start()
    else:
        def WAIT():
            Stop_Event = threading.Event()
            def loading():
                Operation_Is_Running_Instance.CREATE_FRAME()
                while not Stop_Event.is_set():
                    sleep(0.1)
                Operation_Is_Running_Instance.DESTROY_FRAME()
            Loading = threading.Thread(target=loading)
            Loading.start()
            if Loading_Card:
                UPDATE_CARTE()
            elif Boutton_Factice_List != []:
                PIN_FRAME_CREATION(0,0,[],[])
            Stop_Event.set()
        Wait = threading.Thread(target=WAIT)
        Wait.start()
    
    if Fast_Open_Fenetre != None:
        if Fast_Open_Fenetre == 'Script Editor':
            SCRIPT_EDITOR()
        elif Fast_Open_Fenetre == 'Parameter Manager':
            IMPORT_PRESET()
        elif Fast_Open_Fenetre == 'Save Parameter':
            SAVE_PRESET()
        elif Fast_Open_Fenetre == 'Manual Card Connection':
            CARD_MANUAL()
        elif Fast_Open_Fenetre == 'Card Programme Upload':
            CARD_TYPE()

    Fenetre.mainloop() #Boucle de la fenetre principale
    Fenetre = False
    
    #Detruction du fichier temporaire de l'editeur si il na pas etait deja detruit
    if os.path.isfile(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt')):
        os.remove(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'))

portserie = cl.PortSerie()
carte = cl.Carte()
Dechifrage_Ligne = cl.Value_Pin()

portDeLaCarte = None

def lancerApplication():
    MAIN(portserie,None)

app = threading.Thread(target=lancerApplication) 
app.start()

if not __Devellopement__:
    if FalashBang:
        Videosound = AudioFileClip(tl.GET_ABSOLUTE_PATH("video\\Flash bang sound.mp4"))
    else:
        Videosound = AudioFileClip(tl.GET_ABSOLUTE_PATH("video\\Logo.mp4"))
    def SOUND():
        Videosound.preview()
    Sound = threading.Thread(target=SOUND)
    Sound.start()

lignePrecedante = ""
while app.is_alive():
    if portDeLaCarte:
        if portserie.Alive:
            ligneActuelle = portserie.lecture()
            if ligneActuelle != lignePrecedante and ligneActuelle != None:
                #print(ligneActuelle)
                Dechifrage_Ligne.LIGNE_EXTRACTION(ligneActuelle,portserie.identifiantsPinsNumeriques,portserie.identifiantsPinsAnalogiques)
                lignePrecedante = ligneActuelle
            for Item in Pin_Frame_Numerique:
                try:
                    if Item.Id not in Boutton_Factice_List:
                        Item.UPDATE(str(Dechifrage_Ligne.Pin_Numerique_Value[Item.Id]))
                        re.REDIRECT('N'+str(Item.Id),str(Dechifrage_Ligne.Pin_Numerique_Value[Item.Id]))
                except:
                    pass
            for Item in Pin_Frame_Analogique:
                try:
                    if Item.Id not in Boutton_Factice_List:
                        Item.UPDATE(str(round((Dechifrage_Ligne.Pin_Analogique_Value[Item.Id]-20)/10)))
                        re.REDIRECT(str(Item.Id),str(round((Dechifrage_Ligne.Pin_Analogique_Value[Item.Id]-20)/10)))
                except:
                    pass
        else:
            portDeLaCarte = carte.port(0)
    else:
        sleep(0.1)

if portserie.ser is not None:
    portserie.ser.close()

print('_______________________________________Out_______________________________________')
cl.Exit_Class
re.Exit_Redirect
os.system('taskkill /F /IM MAGIC.exe /T')
sys.exit()