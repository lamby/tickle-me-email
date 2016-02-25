tickle-me-email
===============

Toolbox for implementing GTD-like behaviours in your IMAP inbox.


Examples
--------

* Print the current "TODO" list::

    $ tickle-me-email todo

* Send a "TODO" email to yourself, injecting it via IMAP::

    $ tickle-me-email todo Empty recycle bin

  or::

    $ echo Empty recycle bin | tickle-me-email todo -

* "Tickler" file email rotation from ``DELAYED.07`` to ``DELAYED.06`` etc.
  Mail from ``DELAYED.01`` is moved to your main inbox. Use this to "put off"
  emails until a day they are important. To be run daily from ``cron(8)``::

    $ tickle-me-email rotate Inbox.Mail.DELAYED.%02d 1 7 INBOX

* Single-folder version of the above to move email for "after" work into your
  main inbox. Use this when you receive a non-work email during the day. To be
  run at, say, 6:15pm from ``cron(8)``::

    $ tickle-me-email move Inbox.Mail.DELAYED.18h15 INBOX

* Create ``count`` folders based on the specified Python string
  ``template`` starting at ``start``. For example::

    $ create-folders "Inbox.Mail.DELAYED.%02d" 1 14

   ... will create:

    * Inbox.Mail.DELAYED.01
    * Inbox.Mail.DELAYED.02
    * [...]
    * Inbox.Mail.DELAYED.14

* Send draft emails queued in the ``LATER.Evening``, moving them to ``Sent
  Items`` if successful. Use this to avoid getting replies "too" quickly. To be
  run at, say, 6:15pm from ``cron(8)``::

    $ tickle-me-email send-later INBOX.Mail.LATER.Evening "INBOX.Sent Items"

* List all email mailboxes. Use this to find out the "internal" names of your
  IMAP folders::

    $ tickle-me-email list

* Insert an email into your drafts folder::

    $ DRAFT_ATTACHMENT="/path/to/attachment.txt" tickle-me-email drafts - < /path/to/body.txt

* Print the all the current subject lines (eg. for scripting)::

    $ tickle-me-email subjects

* Print the current configuration::

    $ tickle-me-email config


Configuration
-------------

You configure ``tickle-me-email`` via the optional configuration files:

* ``~/.config/tickle-me-email/tickle-me-email.cfg``
* ``/etc/tickle-me-email/tickle-me-email.cfg``

For example::

    [imap]
    server=imap.example.org
    username=lamby
    password=secret
    secure=true

    [smtp]
    server=smtp.example.org
    username=lamby
    password=secret
    secure=true

    [todo]
    mailbox=INBOX
    recipient=TODO <your@email.com>

    [draft]
    mailbox=INBOX.Drafts
    subject=Default draft subject

Alternatively, you can define the following environment variables:

* ``IMAP_SERVER`` (eg. ``imap.example.org``)
* ``IMAP_SECURE`` (eg. ``true``/``false``)
* ``IMAP_USERNAME`` (eg. ``lamby``)
* ``IMAP_PASSWORD`` (eg. ``secret``)

* ``SMTP_SERVER`` (eg. ``smtp.example.org``)
* ``SMTP_SECURE`` (eg. ``true``/``false``)
* ``SMTP_USERNAME`` (eg. ``lamby``)
* ``SMTP_PASSWORD`` (eg. ``secret``)

* ``TODO_EMAIL`` (eg. ``TODO <your@email.com>``)
* ``TODO_PREFIX`` (eg. ``TODO: ``)
* ``TODO_MAILBOX`` (eg. ``INBOX``)

* ``DRAFT_TO`` (eg. ``someone@example.org``)
* ``DRAFT_CC`` (eg. ``someone-else@example.org``)
* ``DRAFT_BCC`` (eg. ``someone-else2@example.org``)
* ``DRAFT_SUBJECT`` (eg. ``Draft subject``)
* ``DRAFT_MAILBOX`` (eg. ``INBOX.Drafts``)
* ``DRAFT_ATTACHMENT`` (eg. ``/path/to/filename.txt``)

* ``SUBJECTS_MAILBOX`` (eg. ``INBOX``)
