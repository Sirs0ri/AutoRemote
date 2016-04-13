
# ToDo (for now)

* [ ] Make the code PEP8 compliant
    * [x] newlines
    * [x] too long lines
    * [ ] replace "\"" with '"'
    * [ ] .format instead of +
    * [x] comments begin with '# '
    * [ ] names of methods
    * [ ] too many arguments
    * [ ] too many variables
    * [ ] Docstrings
* [ ] Comment the code
* [ ] Remove Windows-specific code
* [ ] Remove EventGhost-dependend code


    eg.RegisterPlugin(...)
    folder = eg.ParseString(folder)
    text = eg.ParseString(text)
    dlg = wx.TextEntryDialog(None, eg.ParseString(dialogText),eg.ParseString(dialogTitle), textBoxText)
    eg.actionThread.Func(trItem.SetArguments)(args)
    eg.document.SetIsDirty()
    eg.document.Save()
    return "EventGhost/" + eg.Version.string
    eg.PrintTraceback()
    self.message = self.message.decode(eg.systemEncoding)
    commands = commands.decode(eg.systemEncoding)
    params = params.decode(eg.systemEncoding)
    class SendMessage(eg.ActionBase):
    class RegisterEventGhost(eg.ActionBase):
    class GetLaterUrls(eg.ActionBase):
    class ShowInputDialog(eg.ActionBase):
    class SendNotification(eg.ActionBase):
    class AutoRemote(eg.PluginBase):
    panel = eg.ConfigPanel(self) (7x)
    eg.TriggerEvent(trigger, response)
    eg.TriggerEvent("Input.CANCEL")
    environment.globals = eg.globals.\__dict__
    repeatTimer = eg.ResettableTimer(self.EndLastEvent)
    eg.TriggerEvent("AutoRemote.Updated");
    eg.actionThread.Func(trItem.SetArguments)(args)
    eg.document.SetIsDirty()
    eg.document.Save()
    self.updateCtrl = self.addLine(None,panel.Button("Check for updates (current version: " + eg.plugins.AutoRemote.plugin.info.version + ")"))

* [ ] create a working API
* [ ] Document the API
* [ ] pep8 compliance
