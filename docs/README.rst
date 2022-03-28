############################################
Serverless Lambda Demo Documentation
############################################

.. toctree:: 
    :maxdepth: 2
    :caption: Serverless Lambda Demo Documentation

Links
^^^^^

.. list-table::
    :header-rows: 0

    * - Serverless Framwork (AWS)
      - https://www.serverless.com/framework/docs/providers/aws
    * - FastAPI
      - https://fastapi.tiangolo.com/
    * - Pydantic
      - https://pydantic-docs.helpmanual.io/
    * - Serverless Events
      - https://serverless.com/framework/docs/providers/aws/events/
    * - Serverless Resources
      - https://www.serverless.com/framework/docs/providers/aws/guide/resources


Development
^^^^^^^^^^^

.. note::

    Be sure to set your profile via export AWS_PROFILE=<profile>


*************************
Run / Test Lambda Locally
*************************
.. code-block:: bash

    make offline


*************
Deploy to AWS
*************
.. code-block:: bash

    make deploy

*****************
Destroy Resources
*****************

.. warning:: This will destroy all resources created by the serverless framework.

.. code-block:: bash

    make destroy
    

**********
Tails Logs
**********

.. code-block:: bash

    # tail the web logs
    make logs_web

    # tail the rate lambda function
    make logs_rate

    # tail the cron lambda function
    make logs_cron
