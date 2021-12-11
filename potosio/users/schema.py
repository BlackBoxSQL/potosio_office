import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from .models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class CustomUserQuery(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    users_by_type = graphene.List(
        CustomUserType, usertype=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_users_by_type(root, info, usertype):
        # Querying a single question
        return CustomUser.objects.all().filter(user_type=usertype)


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
