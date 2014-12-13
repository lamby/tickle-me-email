tickle-me-email
===============

Toolbox for implementing GTD-like behaviours in your IMAP inbox.


Examples
--------

"Tickler" file email rotation from (eg.) ``DELAYED.07`` to ``DELAYED.06`` etc.
Mail from ``"DELAYED.01`` is moved to your main inbox. Use this to "put off"
emails until a day they are important. To be run daily from cron(8)::

  $ tickle-me-email rotate Inbox.Mail.DELAYED.%02d INBOX 0 7

----

Single-folder version of the above to move email for "after" work into your
main inbox. Use this when you receive a non-work email during the day. To be
run at 6:15pm from cron(8)::

  $ tickle-me-email rotate Inbox.Mail.DELAYED.18h15 INBOX 0 1

----

Send draft emails queued in the ``LATER.Evening``, moving them to ``Sent
Items`` if successful. Use this to avoid getting replies "too" quickly. To be
run at, say, 6:15pm from cron(8)::

 $ tickle-me-email send_later INBOX.Mail.LATER.Evening "INBOX.Sent Items"

----

List all email inboxes. Use this to find out the "internal" names of your IMAP
inbox::

   $ tickle-me-email list


Configuration
-------------

You need to set the following environment variables:

 * ``IMAP_SERVER`` (eg. ``imap.example.org``)
 * ``IMAP_USERNAME`` (eg. ``lamby``)
 * ``IMAP_PASSWORD`` (eg. ``secret``)

 * ``SMTP_SERVER`` (eg. ``smtp.example.org``)
 * ``SMTP_USERNAME`` (eg. ``lamby``)
 * ``SMTP_PASSWORD`` (eg. ``secret``)
