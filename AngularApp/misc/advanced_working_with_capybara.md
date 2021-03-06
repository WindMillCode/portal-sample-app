# Introduction

The Ruby bindings for Selenium/WebDriver are available as the [selenium-webdriver](http://rubygems.org/gems/selenium-webdriver) gem. The web page explains how to install the selenium-webdriver gem. On Mac OSX and linux you may need to prefix the rest of the command with the `sudo` command if the installation fails because of security restrictions on your computer.

There are many other Selenium gems out there, but this is the only official, maintained gem. If you're looking for a slightly higher level API built on the same technology, you may want to check out [watir-webdriver](http://watirwebdriver.com/) or [capybara](https://github.com/jnicklas/capybara).

The bindings support Ruby 1.9.2 through 2.1.

  * [API docs](http://selenium.googlecode.com/git/docs/api/rb/index.html)
  * [Changelog](http://selenium.googlecode.com/git/rb/CHANGES)

The gem also includes the older selenium-client gem for use with Selenium RC. When reading the docs, keep in mind that these two namespaces refer to different APIs:

  * `Selenium::WebDriver` - the WebDriver API
  * `Selenium::Client` - Selenium RC API (previously released as the selenium-client gem)

The WebDriver API is the successor to the Selenium RC API. For people who don't have a significant investment in the legacy API, we recommend starting directly with `Selenium::WebDriver`, and focusing on the two main classes, `Selenium::WebDriver::Driver` and `Selenium::WebDriver::Element`. This is the entry point to the whole WebDriver API.

For people who already have tests written against the Selenium RC API, it's possible to use [WebDriver-backed Selenium](#-backed_Selenium.md) to ease the migration. The rest of this document deals with `Selenium::WebDriver` exclusively.

If you're interested in developing the Ruby bindings for Selenium, see the RubyDevelopment page.

# API Example

The bindings provide a slightly rubified version of the WebDriver API:

```
require "selenium-webdriver"

driver = Selenium::WebDriver.for :firefox
driver.navigate.to "http://google.com"

element = driver.find_element(:name, 'q')
element.send_keys "Hello WebDriver!"
element.submit

puts driver.title

driver.quit
```

Driver examples:

```
# execute arbitrary javascript
puts driver.execute_script("return window.location.pathname")

# pass elements between Ruby and JavaScript
element = driver.execute_script("return document.body")
driver.execute_script("return arguments[0].tagName", element) #=> "BODY"

# wait for a specific element to show up
wait = Selenium::WebDriver::Wait.new(:timeout => 10) # seconds
wait.until { driver.find_element(:id => "foo") }

# switch to a frame
driver.switch_to.frame "some-frame" # name or id
driver.switch_to.frame driver.find_element(:id, 'some-frame') # frame element

# switch back to the main document
driver.switch_to.default_content

# repositionning and resizing browser window:
driver.manage.window.move_to(300, 400)
driver.manage.window.resize_to(500, 800)
driver.manage.window.maximize
```

Element examples:

```
# get an attribute
class_name = element.attribute("class")

# is the element visible on the page?
element.displayed?

# click the element
element.click

# get the element location
element.location

# scroll the element into view, then return its location
element.location_once_scrolled_into_view

# get the width and height of an element
element.size

# press space on an element - see Selenium::WebDriver::Keys for possible values
element.send_keys :space

# get the text of an element
element.text
```


Advanced user interactions (see [ActionBuilder](http://selenium.googlecode.com/svn/trunk/docs/api/rb/Selenium/WebDriver/ActionBuilder.html)):

```
driver.action.key_down(:shift).
              click(element).
              double_click(second_element).
              key_up(:shift).
              drag_and_drop(element, third_element).
              perform
```


## IE

Make sure that _Internet Options_ ??? _Security_ has the same _Protected Mode_ setting (on or off, it doesn't matter as long as it is the same value) for all zones.

## Chrome

### Command line switches

For a list of switches, see [this list](http://peter.sh/experiments/chromium-command-line-switches/).

```
driver = Selenium::WebDriver.for :chrome, :switches => %w[--ignore-certificate-errors --disable-popup-blocking --disable-translate]
```

### Tweaking profile preferences

For a list of prefs, see [pref\_names.cc](http://src.chromium.org/svn/trunk/src/chrome/common/pref_names.cc).

Using chromedriver 1:

```
profile = Selenium::WebDriver::Chrome::Profile.new
profile['download.prompt_for_download'] = false
profile['download.default_directory'] = "/path/to/dir"

driver = Selenium::WebDriver.for :chrome, :profile => profile
```

Using chromdriver 2 (supported since selenium-webdriver 2.37):

```
prefs = {
  :download => {
    :prompt_for_download => false, 
    :default_directory => "/path/to/dir"
  }
}

driver = Selenium::WebDriver.for :chrome, :prefs => prefs
```

See also ChromeDriver.

## Remote

The RemoteWebDriver makes it easy to control a browser running on another machine. Download the jar (from [Downloads](http://code.google.com/p/selenium/downloads/list)) and launch the server:

`java -jar selenium-server-standalone.jar`

Then connect to it from Ruby

```
driver = Selenium::WebDriver.for(:remote)
```

By default, this connects to the server running on localhost:4444 and opens Firefox. To connect to another machine, use the `:url` option:

```
driver = Selenium::WebDriver.for(:remote, :url => "http://myserver:4444/wd/hub")
```

To launch another browser, use the :desired\_capabilities option:

```
driver = Selenium::WebDriver.for(:remote, :desired_capabilities => :chrome)
```

You can also pass an instance of `Selenium::WebDriver::Remote::Capabilities`, e.g.:

```
caps = Selenium::WebDriver::Remote::Capabilities.htmlunit(:javascript_enabled => true)
driver = Selenium::WebDriver.for(:remote, :desired_capabilities => caps)
```

You can change arbitrary capabilities:

```
caps = Selenium::WebDriver::Remote::Capabilities.internet_explorer
caps['enablePersistentHover'] = false

driver = Selenium::WebDriver.for(:remote, :desired_capabilities => caps)
```

You may want to set the proxy settings of the remote browser (this currently only works for Firefox):

```
caps = Selenium::WebDriver::Remote::Capabilities.firefox(:proxy => Selenium::WebDriver::Proxy.new(:http => "myproxyaddress:8080"))
driver = Selenium::WebDriver.for(:remote, :desired_capabilities => caps)
```

Or if you have a proxy in front of the remote server:

```
client = Selenium::WebDriver::Remote::Http::Default.new
client.proxy = Selenium::Proxy.new(:http => "proxy.org:8080")

driver = Selenium::WebDriver.for(:remote, :http_client => client)
```

See [`Selenium::WebDriver::Proxy`](http://code.google.com/p/selenium/source/browse/trunk/rb/lib/selenium/webdriver/common/proxy.rb) for more options.

For the remote Firefox driver you can configure the profile, see the section [Tweaking Firefox preferences](#Tweaking_Firefox_preferences.md).

## Firefox

The FirefoxDriver lets you configure the profile used.

### Adding an extension

It's often useful to have Firebug available in the Firefox instance launched by WebDriver:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile.add_extension("/path/to/firebug.xpi")

driver = Selenium::WebDriver.for :firefox, :profile => profile
```

### Using an existing profile

You can use an existing profile as a template for the WebDriver profile by passing the profile name (see `firefox -ProfileManager` to set up custom profiles.)

```
driver = Selenium::WebDriver.for(:firefox, :profile => "my-existing-profile")
```

If you want to use your default profile, pass `:profile => "default"`

You can also get a Profile instance for an existing profile and tweak its preferences. This does not modify the existing profile, only the one used by WebDriver.

```
default_profile = Selenium::WebDriver::Firefox::Profile.from_name "default"
default_profile.native_events = true

driver = Selenium::WebDriver.for(:firefox, :profile => default_profile)
```

### Tweaking Firefox preferences

Use a proxy:

```
profile = Selenium::WebDriver::Firefox::Profile.new
proxy = Selenium::WebDriver::Proxy.new(:http => "proxy.org:8080")
profile.proxy = proxy

driver = Selenium::WebDriver.for :firefox, :profile => profile
```

Automatically download files to a given folder:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile['browser.download.dir'] = "/tmp/webdriver-downloads"
profile['browser.download.folderList'] = 2
profile['browser.helperApps.neverAsk.saveToDisk'] = "application/pdf"
profile['pdfjs.disabled'] = true

driver = Selenium::WebDriver.for :firefox, :profile => profile
```

If you are using the remote driver you can still configure the Firefox profile:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile['foo.bar'] = true

capabilities = Selenium::WebDriver::Remote::Capabilities.firefox(:firefox_profile => profile)
driver = Selenium::WebDriver.for :remote, :desired_capabilities => capabilities
```

For a list of possible preferences, see [this page](http://preferential.mozdev.org/preferences.html).

### Custom Firefox path

If your Firefox executable is in a non-standard location:

```
Selenium::WebDriver::Firefox.path = "/path/to/firefox"
driver = Selenium::WebDriver.for :firefox
```

### SSL Certificates

The Firefox driver ignores invalid SSL certificates by default. If this is not the behaviour you want, you can do:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile.secure_ssl = true

driver = Selenium::WebDriver.for :firefox, :profile => profile
```

There is an edge case where the default SSL certificate check will not work correctly. WebDriver assumes that the certificate is untrusted whenever there's a problem, which means a certificate from a trusted issuer but with a hostname mismatch (e.g. a production certificate in a test environment) will not be correctly ovverriden.  See UntrustedSSLCertificates for more on why this is. To work around it, tell the Firefox driver to not assume the issuer is untrusted:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile.assume_untrusted_certificate_issuer = false
driver = Selenium::WebDriver.for :firefox, :profile => profile
```

Not that Profile#secure\_ssl remains set to the default value of true in the above example.



### Native events

Native events are enabled by default on Windows. To turn them off:

```
profile = Selenium::WebDriver::Firefox::Profile.new
profile.native_events = false

driver = Selenium::WebDriver.for(:firefox, :profile => profile)
```

Experimental support for native events is available on Linux. Set `profile.native_events = true` to turn this on.

## Opera

The OperaDriver is always run as a RemoteWebDriver server which the Ruby bindings connect to.

To get started, first [download](http://code.google.com/p/selenium/downloads/list) the _selenium-server-standalone_ jar and set the `SELENIUM_SERVER_JAR` environmental variable to point to its location:

`export SELENIUM_SERVER_JAR=/path/to/server-standalone.jar`

Then you can simply create a new instance of `Selenium::WebDriver` with the `:opera` option:

```
driver = Selenium::WebDriver.for :opera
driver.navigate.to 'http://opera.com/'
```

## Safari

A Safari driver is available as of v2.21. See SafariDriver for details on usage. From Ruby:

```
driver = Selenium::WebDriver.for :safari
driver.navigate.to "http://apple.com"
```

To configure the driver, use the Selenium::WebDriver::Safari::Options class (available since 2.40.0):

```
opts = Selenium::WebDriver::Safari::Options.new
opts.add_extension '/my/custom/extension.safariextz'

driver = Selenium::WebDriver.for :safari, :options => opts
```

This class can also be used to configure a remote driver:

```
opts = Selenium::WebDriver::Safari::Options.new
opts.port = 54321
opts.add_extension '/my/custom/extension.safariextz'
opts.clean_session = true

driver = Selenium::WebDriver.for :remote, :desired_capabilities => opts.to_capabilities
```

## Timeouts

### Implicit waits

WebDriver lets you configure implicit waits, so that a call to `#find_element` will wait for a specified amount of time before raising a `NoSuchElementError`:

```
  driver = Selenium::WebDriver.for :firefox
  driver.manage.timeouts.implicit_wait = 3 # seconds
```

### Explicit waits

Use the Wait class to explicitly wait for some condition:

```
  wait = Selenium::WebDriver::Wait.new(:timeout => 3)
  wait.until { driver.find_element(:id => "cheese").displayed? }
```

### Internal timeouts

Internally, WebDriver uses HTTP to communicate with a lot of the drivers (the JsonWireProtocol). By default, `Net::HTTP` from Ruby's standard library is used, which has a default timeout of 60 seconds. If you call e.g. `Driver#get`, `Driver#click` on a page that takes more than 60 seconds to load, you'll see a `Timeout::Error` raised from `Net::HTTP`. You can configure this timeout (before launching a browser) by doing:

```
  client = Selenium::WebDriver::Remote::Http::Default.new
  client.timeout = 120 # seconds
  driver = Selenium::WebDriver.for(:remote, :http_client => client)
```


## JavaScript dialogs

You can use webdriver to handle Javascript `alert()`, `prompt()` and `confirm()` dialogs.
The API for all three is the same.

Note: At this time alert handling is only available in Firefox and IE (or in those browsers through the remote server), and only alerts that are generated post onload can be captured.

```
require "selenium-webdriver"

driver = Selenium::WebDriver.for :firefox
driver.navigate.to "http://mysite.com/page_with_alert.html"

driver.find_element(:name, 'element_with_alert_javascript').click
a = driver.switch_to.alert
if a.text == 'A value you are looking for'
  a.dismiss
else
  a.accept
end

```

## Using Curb or your own HTTP client

For internal HTTP communication, `Net::HTTP` is used by default. If you e.g. have the [Curb gem](https://rubygems.org/gems/curb) installed, you can switch to it by doing:

```
require 'selenium/webdriver/remote/http/curb'

client = Selenium::WebDriver::Remote::Http::Curb.new
driver = Selenium::WebDriver.for(:firefox, :http_client => client)
```

If you have the [net-http-persistent gem](https://github.com/drbrain/net-http-persistent) installed, you can (as of 0.1.3) similarly use "selenium/webdriver/remote/http/persistent" to get keep-alive connections. This will significantly reduce the ephemeral ports usage of WebDriver, which is useful in [some contexts](ScalingWebDriver.md). Note that this currently only works with the remote Java server (the other servers doesn't yet support keep-alive).

## WebDriver-backed Selenium

If you already have tests written against the RC API, the Selenium server (since version 2.19) gives you ability to run your existing code backed by a WebDriver instance. This can help the migration to WebDriver since it allows you to mix and match the two APIs in the same test. Here's an example:

```
require 'selenium/webdriver'
require 'selenium/client'
require 'selenium/server'

server = Selenium::Server.new("selenium-server-standalone-2.19.0.jar", :background => true)
server.start

begin
  selenium = Selenium::Client::Driver.new :host    => "localhost",
                                          :port    => 4444,
                                          :url     => "http://google.com",
                                          :browser => "*webdriver"
  driver = Selenium::WebDriver.for :remote, :url => "http://localhost:4444/wd/hub/"

  selenium.start :driver => driver
  selenium.open "/"
  selenium.type 'q', 'webdriver-backed selenium'

  p driver.title == selenium.title

  selenium.stop
ensure
  server.stop
end
```

The opposite of this, a Selenium-backed WebDriver, is not available from Ruby at the moment.
