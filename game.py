Package Control Messages
========================

EasyClangComplete
-----------------

  ################################
  ## EasyClangComplete v. 3.3.2 ##
  ################################
  
  # Bug fixes and improvements #
  - Make every action of the plugin use a custom thread pool. Before some parts would use the sublime text internal worker thread. Now everything spawns a separate thread from a pool. Please report if you see regressions.
  - Fix blocking other plugins when running long cmake operation.
  
  # Support it #
  It takes time and effort to develop a plugin. Consider contributing your time by submitting a pull request on a feature you like or buy me a coffee:
  https://github.com/niosus/EasyClangComplete#support-it

  ################################
  ## EasyClangComplete v. 3.3.1 ##
  ################################
  
  # Bug fixes #
  - Version 3.3.0 introduced a crash for those who don't use libclang.
  - This update fixes the issue
  - Core organization improvements

  ################################
  ## EasyClangComplete v. 3.3.0 ##
  ################################
  
  # New feature! Yay! #
  - @simia added function and variable definition popup on mouse hover.
  - Just hover your mouse over a function to see its signature + short comments
    if present. Only works with when `use_libclang` = "true".
