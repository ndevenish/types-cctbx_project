class environment:
    dispatcher_name: str
    def set_os_environ_all_dist(self) -> None:
        """Set environment variable <NAME>_DIST for all active *tbx modules"""
    def under_base(self, path: str, return_relocatable_path: bool = ...) -> str:
        """
        Return an absolute path under the environment base, whether this is
        base/ or conda_base/ relative to the build.
        """
