def get_exp(exp):
    if(exp == "cmd" or exp == "css" or exp == "csv" or
       exp == "html" or exp == "javascript" or exp == "plain" or
       exp == "php" or exp == "xml" or exp == "markdown" or
       exp == "cache-manifest"):
        return "text/" + exp
    if(exp == "png" or exp == "gif" or exp == "jpeg" or
       exp == "pjpeg" or exp == "png" or exp == "svg+xml" or
       exp == "tiff" or exp == "vnd.microsoft.icon" or
       exp == "vnd.wap.wbmp" or exp == "webp"):
        return "image/" + exp
    if(exp == "mpeg" or exp == "mp4" or exp == "ogg" or
       exp == "quicktime" or exp == "webm" or exp == "x-ms-wmv" or
       exp == "x-flv" or exp == "3gpp" or exp == "3gpp2"):
        return "video/" + exp
    return "application/" + exp