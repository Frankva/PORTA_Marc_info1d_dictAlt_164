"""
    Fichier : gestion_personnes_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterPersonnes(FlaskForm):
    """
        Dans le formulaire "personnes_ajouter_wtf.html" on impose que le champ
        soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_genre_regexp = ("^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za"
                        "-zÀ-ÖØ-öø-ÿ]+$")
    nom_personne_wtf = StringField("Saisir le nom de la personne",
            validators=[Length(min=2, max=20, message="min 2 max 20"),
            Regexp(nom_genre_regexp, message="Pas de chiffres, de caractères "
            "spéciaux, d'espace à double, de double apostrophe, de double"
            " trait union")])
    submit = SubmitField("Enregistrer personne")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    # nom_genre_update_regexp = ("^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]"
    #                            "?[A-Za-zÀ-ÖØ-öø-ÿ]+$")
    nom_genre_update_regexp = ".*"
    nom_genre_update_wtf = StringField("Saisir le nom de la personne",
            validators=[Length(min=2, max=20, message="min 2 max 20"),
            Regexp(nom_genre_update_regexp, message="Pas de chiffres, de "
            "caractères spéciaux, d'espace à double, de double apostrophe, de "
            "double trait union")])
    date_genre_wtf_essai = DateField("Essai date", validators=[
              InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    submit = SubmitField("Sauvegarder la personne")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")