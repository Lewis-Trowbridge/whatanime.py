class WhatanimeError(Exception):

    """
    Base exception class for this module
    """
    pass


class QuotaExceededError(WhatanimeError):
    """
    Error for when the daily quota for requests has been exceeded
    """
    pass


class ImageSizeTooLargeError(WhatanimeError):
    """
    Error for when an image uploaded to trace.moe was too large
    """
    pass


class APIError(WhatanimeError):
    """
    Error for when an error occurs on trace.moe's side
    """