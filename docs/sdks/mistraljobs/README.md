# MistralJobs
(*batch.jobs*)

## Overview

### Available Operations

* [list](#list) - Get Batch Jobs
* [create](#create) - Create Batch Job
* [get](#get) - Get Batch Job
* [cancel](#cancel) - Cancel Batch Job

## list

Get a list of batch jobs for your organization and user.

### Example Usage

```python
from mistralai import Mistral
import os


with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.batch.jobs.list(page=0, page_size=100, created_by_me=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `page`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `page_size`                                                          | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `model`                                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `metadata`                                                           | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_after`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_by_me`                                                      | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `status`                                                             | List[[models.BatchJobStatus](../../models/batchjobstatus.md)]        | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.BatchJobsOut](../../models/batchjobsout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create

Create a new batch job, it will be queued for processing.

### Example Usage

```python
from mistralai import Mistral
import os


with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.batch.jobs.create(input_files=[
        "fe3343a2-3b8d-404b-ba32-a78dede2614a",
    ], endpoint="/v1/moderations", model="Altima", timeout_hours=24)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `input_files`                                                       | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `endpoint`                                                          | [models.APIEndpoint](../../models/apiendpoint.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `model`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metadata`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `timeout_hours`                                                     | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get a batch job details by its UUID.

### Example Usage

```python
from mistralai import Mistral
import os


with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.batch.jobs.get(job_id="4017dc9f-b629-42f4-9700-8c681b9e7f0f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## cancel

Request the cancellation of a batch job.

### Example Usage

```python
from mistralai import Mistral
import os


with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.batch.jobs.cancel(job_id="4fb29d1c-535b-4f0a-a1cb-2167f86da569")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |