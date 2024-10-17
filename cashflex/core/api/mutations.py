import graphene
import environ
from cashflex.core.api.inputs import *
from cashflex.core.api.schema import *
from cashflex.core.models import *
env = environ.Env()


class CreatePartner(graphene.Mutation):
    class Arguments:
        input = PartnerInput(required=True)

    partner = graphene.Field(PartnerObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        partner = Partner.objects.create(
            name=input.name,
            slug=input.slug,
            discription=input.discription,
            website=input.website,
            image=input.image,
            is_active=input.is_active
        )

        return CreatePartner(partner=partner, success=True)


class UpdatePartner(graphene.Mutation):
    class Arguments:
        input = UpdatePartnerInput()

    partner = graphene.Field(PartnerObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        partner = Partner.objects.get(pk=input.id)
        if input.name:
            partner.name = input.name
        if input.slug:
            partner.slug = input.slug
        if input.discription:
            partner.discription = input.discription
        if input.website:
            partner.website = input.website
        if input.image:
            partner.image = input.image
        if input.is_active:
            partner.is_active = input.is_active

        partner.save()
        return UpdatePartner(partner=partner, success=True)


class DeletePartner(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    partner = graphene.Field(PartnerObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        partner = Partner.objects.get(pk=id)
        partner.delete()
        return DeletePartner(success=True)


class CreateFAQCategory(graphene.Mutation):
    class Arguments:
        input = FAQCategoryInput()

    faq_category = graphene.Field(FAQCategoryObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        faq_category = FAQCategory.objects.create(
            name=input.name,
            slug=input.slug,
        )
        faq_category.save()
        return CreateFAQCategory(faq_category=faq_category, success=True)


class UpdateFAQCategory(graphene.Mutation):
    class Arguments:
        input = UpdateFAQCategoryInput()

    faq_category = graphene.Field(FAQCategoryObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        faq_category = FAQCategory.objects.get(pk=input.id)
        if input.name:
            faq_category.name = input.name
        if input.slug:
            faq_category.slug = input.slug
        faq_category.save()
        return UpdateFAQCategory(faq_category=faq_category, success=True)


class DeleteFAQCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    faq_category = graphene.Field(FAQCategoryObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        faq_category = FAQCategory.objects.get(pk=id)
        faq_category.delete()
        return DeleteFAQCategory(success=True)


class CreateFAQ(graphene.Mutation):
    class Arguments:
        input = FAQInput()

    faq = graphene.Field(FAQObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        faq = FAQ.objects.create(
            question=input.question,
            slug=input.slug,
            answer=input.answer,
            category=FAQCategory.objects.get(pk=input.category),
            is_active=input.is_active
        )
        faq.save()
        return CreateFAQ(faq=faq, success=True)


class UpdateFAQ(graphene.Mutation):
    class Arguments:
        input = UpdateFAQInput()

    faq = graphene.Field(FAQObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        faq = FAQ.objects.get(pk=input.id)
        if input.question:
            faq.question = input.question
        if input.slug:
            faq.slug = input.slug
        if input.answer:
            faq.answer = input.answer
        if input.category:
            faq.category = FAQCategory.objects.get(pk=input.category)
        if input.is_active:
            faq.is_active = input.is_active
        faq.save()
        return UpdateFAQ(faq=faq, success=True)


class DeleteFAQ(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    faq = graphene.Field(FAQObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        faq = FAQ.objects.get(pk=id)
        faq.delete()
        return DeleteFAQ(success=True)


class TrainingTypeMutation(graphene.Mutation):
    class Arguments:
        input = TrainingTypeInput()

    training_type = graphene.Field(TrainingTypeObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        training_type = TrainingType.objects.create(
            name=input.name,
            slug=input.slug,
            is_active=input.is_active
        )
        training_type.save()
        return TrainingTypeMutation(training_type=training_type, success=True)


class UpdateTrainingType(graphene.Mutation):
    class Arguments:
        input = UpdateTrainingTypeInput()

    training_type = graphene.Field(TrainingTypeObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        training_type = TrainingType.objects.get(pk=input.id)
        if input.name:
            training_type.name = input.name
        if input.slug:
            training_type.slug = input.slug
        if input.is_active:
            training_type.is_active = input.is_active
        training_type.save()
        return UpdateTrainingType(training_type=training_type, success=True)


class DeleteTrainingType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    training_type = graphene.Field(TrainingTypeObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        training_type = TrainingType.objects.get(pk=id)
        training_type.delete()
        return DeleteTrainingType(success=True)


class TrainingMutation(graphene.Mutation):
    class Arguments:
        input = TrainingInput()

    training = graphene.Field(TrainingObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        training = Training.objects.create(
            title=input.title,
            slug=input.slug,
            description=input.description,
            video=input.video,
            type=TrainingType.objects.get(pk=input.type),
            is_active=input.is_active
        )
        training.save()
        return TrainingMutation(training=training, success=True)


class UpdateTraining(graphene.Mutation):
    class Arguments:
        input = UpdateTrainingInput()

    training = graphene.Field(TrainingObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        training = Training.objects.get(pk=input.id)
        if input.title:
            training.title = input.title
        if input.slug:
            training.slug = input.slug
        if input.description:
            training.description = input.description
        if input.video:
            training.video = input.video
        if input.type:
            training.type = TrainingType.objects.get(pk=input.type)
        if input.is_active:
            training.is_active = input.is_active
        training.save()
        return UpdateTraining(training=training, success=True)


class DeleteTraining(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    training = graphene.Field(TrainingObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        training = Training.objects.get(pk=id)
        training.delete()
        return DeleteTraining(success=True)


class ContactMutation(graphene.Mutation):
    class Arguments:
        input = ContactInput()

    contact = graphene.Field(ContactObjectType)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        contact = Contact.objects.create(
            name=input.name,
            email=input.email,
            phone=input.phone,
            message=input.message
        )
        contact.save()
        return ContactMutation(contact=contact, success=True)


class SocialMediaMutation(graphene.Mutation):
    class Arguments:
        input = SocialMediaInput()

    social_media = graphene.Field(SocialMediaObjectType)
    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, input=None):
        social_media = SocialMedia.objects.create(
            platform=input.platform,
            url=input.url,
            icon=input.icon,
        )
        return SocialMediaMutation(social_media=social_media, success=True, message="Social Media Added Successfully")


class UpdateSocialMedia(graphene.Mutation):
    class Arguments:
        input = UpdateSocialMediaInput()

    social_media = graphene.Field(SocialMediaObjectType)
    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, input=None):
        social_media = SocialMedia.objects.get(pk=input.id)
        if input.platform:
            social_media.platform = input.platform
        if input.url:
            social_media.url = input.url
        if input.icon:
            social_media.icon = input.icon
        social_media.save()
        return UpdateSocialMedia(social_media=social_media, success=True, message="Social Media Updated Successfully")


class CoreMutation(graphene.ObjectType):
    create_partner = CreatePartner.Field()
    update_partner = UpdatePartner.Field()
    delete_partner = DeletePartner.Field()
    faq_category_mutation = CreateFAQCategory.Field()
    update_faq_category = UpdateFAQCategory.Field()
    delete_faq_category = DeleteFAQCategory.Field()
    create_faq = CreateFAQ.Field()
    update_faq = UpdateFAQ.Field()
    delete_faq = DeleteFAQ.Field()
    training_type_mutation = TrainingTypeMutation.Field()
    update_training_type = UpdateTrainingType.Field()
    delete_training_type = DeleteTrainingType.Field()
    training_mutation = TrainingMutation.Field()
    update_training = UpdateTraining.Field()
    delete_training = DeleteTraining.Field()
    contact_mutation = ContactMutation.Field()
    create_social_media = SocialMediaMutation.Field()
    update_social_media = UpdateSocialMedia.Field()
