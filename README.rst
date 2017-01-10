exsim
=====

|  |Build Status|  |Code Health|  |Coverage|  |PyPI|  |Python|


Introduction
------------

# Exchange Simulator
#
# Run a basic event loop.
# Listen on a TCP socket, and accept connections.
# Decode messages according to protocol module for that session.
# Dispatch messages via central dispatcher.
# Support for automatic test-requests/heartbeats.
# Messages can be queued for manual handling.
# Policy modules can be loaded for automatic message handling.
# Basic matching engine will manage books, publish data, and match orders.


# Milestone 1
#
# - Accept protocol market data and trade flow connections
#   - Connect
#   - Disconnect
# - Accept management connections.
#   - Decide on a protocol.
#     - REST?
# - Read and queue data
# - Send data
# - Timeouts
# - Hearbeats
# - Logon & Logout
#
# This is sufficient to handle basic message flow to/from a venue.
# It's also basically a REST API on the side of RobotNPS ...

# Also needed is the client-side:
# - Use requests module.
#   - Completely synchronous RPC-style.
# - Spawn simulator process in background?

# Next thing needed is a pricing module: in order to generate a useful
# pricing stream, we need to have useful prices.  So that can either
# be managed directly via the API, or could track an externally
# sourced price stream.

License
-------

exsim is licensed under the GNU Public License.

While this is not legal advice, in short this means you're free to use
this code at no cost.  You may also change it and run the modifified
version, or integrate it with other code, but if you do you must not
distribute the changed code or a system that integrates this software
unless it is also made available under the GPL license.

Contributing
------------

Comments, suggestions, bug reports, bug fixes -- all contributions to
this project are welcomed.  See the project's `GitHub
<https://github.com/da4089/exsim>`_ page for access to the latest
source code, and please open an `issue
<https://github.com/da4089/exsim/issues>`_ for comments, suggestions,
and bugs.




.. |Build Status| image:: https://travis-ci.org/da4089/exsim.svg?branch=master
    :target: https://travis-ci.org/da4089/exsim
    :alt: Build status
.. |Code Health| image:: https://landscape.io/github/da4089/exsim/master/landscape.svg?style=flat
    :target: https://landscape.io/github/da4089/exsim/master
    :alt: Code Health
.. |Coverage| image:: https://coveralls.io/repos/github/da4089/exsim/badge.svg?branch=master
    :target: https://coveralls.io/github/da4089/exsim?branch=master
    :alt: Coverage
.. |PyPI| image:: https://img.shields.io/pypi/v/exsim.svg
    :target: https://pypi.python.org/pypi/exsim
    :alt: PyPI
.. |Python| image:: https://img.shields.io/pypi/pyversions/exsim.svg
    :target: https://pypi.python.org/pypi/exsim
    :alt: Python
