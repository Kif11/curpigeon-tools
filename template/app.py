import string
from lib.pathlib import Path

class Template(object):

    def __init__(self,
                 project_path,
                 asset_path,
                 shot_path,
                 script_path,
                 scene_path,
                 sequence,
                 shot,
                 user,
                 version):

        self._shot_code = 'SQ${sq}_SH${sh}'
        self._nuke_name = '${shot_code}_${version}_${user}.nk'
        self._maya_name = '${shot_code}_${version}_${user}.ma'
        self._padding = r'%02d'

        self.project_path = project_path
        self.asset_path = asset_path
        self.shot_path = shot_path
        self.script_path = script_path
        self.scene_path = scene_path

        self.shot = shot
        self.sequence = sequence

        self.version = version
        self.user = user

        self._shot_name = ''
        self._asset_name = ''

    def expand_name(self, template_name, **kwargs):
        t = string.Template(template_name)
        return t.substitute(**kwargs)

    def absolute(self, path):
        return self._project_path / path

    @property
    def project_path(self):
        return self._project_path
    @project_path.setter
    def project_path(self, path):
        self._project_path = Path(path)

    @property
    def shot(self):
        return self._shot
    @shot.setter
    def shot(self, value):
        self._shot = value

    @property
    def sequence(self):
        return self._sequence
    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, value):
        self._version = self._padding % value

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value):
        self._user = value.upper()[:-3]

    @property
    def shot_code(self):
        return self.expand_name(self._shot_code,
                                sq=self._sequence,
                                sh=self._shot)

    @property
    def nuke_name(self):
        return self.expand_name(self._nuke_name,
                                shot_code=self.shot_code,
                                version=self.version,
                                user=self.user)

    @property
    def asset_path(self):
        return self.absolute(self._asset_path)
    @asset_path.setter
    def asset_path(self, path):
        self._asset_path = Path(path)

    @property
    def script_path(self):
        return self.absolute(self._script_path)
    @script_path.setter
    def script_path(self, path):
        self._script_path = Path(path)


    @property
    def scene_path(self):
        return self.absolute(self._scene_path)
    @scene_path.setter
    def scene_path(self, path):
        self._scene_path = Path(path)

if __name__ == '__main__':

    t = Template(project_path='//180net1/Collab/tbertino_Curpigeon/Curpigeon_Project',
                 asset_path='Assets',
                 shot_path='Shots',
                 scene_path='Scene',
                 sequence=1,
                 shot=2,
                 version=4,
                 user='kirill')

    # t.project_path = '/User/admin/Desctop/CP'
    # t.sequence = '01'
    # t.shot = '02'
    # t.version = 4
    # t.user = 'kirill'

    print t.shot_code
    print t.nuke_name
    print t.asset_path
    print t.scene_path
