from gabblep.core.proto_values.irods_common_enums import AuthScheme

class IrodsAccount():

    def __init__(self, host, zone, user_name, password,  port=1247, admin_user_for_proxy='',
                 admin_password_for_proxy='', default_storage_resource='', auth_scheme=AuthScheme.STANDARD):
        """General initializer of an IrodsAccount

                Args:
                    :param str host: iRODS host name
                    :param str zone: iRODS zone
                    :param str user_name: iRODS user name (if proxied this is the name of the user to run as
                    :param str password: iRODS user password
                    :param int port: iRODS port (default 1247)
                    :param str admin_user_for_proxy: optional admin user name that will be used to generate a proxy
                        account
                    :param str admin_password_for_proxy: optional password for admin to generate a proxy account
                    :param str default_storage_resource: optional default resource for operations
                    :param AuthScheme auth_scheme: emum value describing the authentication scheme

                """
        self.host = host
        self.port = port
        self.zone = zone
        self.user_name = user_name
        self.password = password
        self.admin_user_for_proxy = admin_user_for_proxy
        self.admin_password_for_proxy = admin_password_for_proxy
        self.default_storage_resource = default_storage_resource
        self.auth_scheme = auth_scheme

        


