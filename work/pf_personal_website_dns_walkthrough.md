# DNS Walkthrough for my personal website

## What a CNAME record is

A CNAME (Canonical Name) record is a DNS record that points one hostname to another hostname. It does not point directly to an IP address. It says, in effect, "this name is an alias of that name."

For my future FlyRank setup, the record would look conceptually like this:

- Host/name: my subdomain (for example, yourname.flyrank.ai)
- Type: CNAME
- Value/target: the hostname my website host gives me (for example, yourname.netlify.app)

That means anyone who visits my FlyRank subdomain is redirected at the DNS level to the host-managed website endpoint.

## What value my CNAME will hold

When my FlyRank subdomain is provisioned, Ops will provide or confirm the exact target. If I use Netlify, the CNAME target is typically my Netlify site hostname, such as yourname.netlify.app.

So the practical rule is:

- CNAME value equals the hosting provider hostname, not an IP, and not a random URL path.

## What happens when someone types my address

Here is the full flow in plain language:

1. A person types my address in their browser, for example yourname.flyrank.ai.
2. The browser asks a DNS resolver (usually from the user ISP, company, or public DNS service) for the IP behind that name.
3. If the resolver does not already know the answer from cache, it asks the authoritative nameservers for flyrank.ai.
4. The authoritative nameserver returns the DNS record for my subdomain. In this case it returns a CNAME pointing to my hosting name, such as yourname.netlify.app.
5. The resolver then looks up that target hostname and gets the final address information required to reach the host.
6. The resolver returns that answer to the browser.
7. The browser connects to the hosting platform and requests the site over HTTPS.
8. The host returns the website content, and the browser shows the page with a padlock if the certificate is valid.

## Why propagation can take time

DNS answers are cached for a period called TTL (time to live). Even after adding or changing a CNAME, some resolvers keep the old answer until TTL expires. That is why a domain update can appear to work for one person and not another for a short period.

## My capstone-time checklist

1. In hosting settings, add custom domain yourname.flyrank.ai.
2. Confirm the host shows the expected DNS target value.
3. Ensure the FlyRank DNS CNAME points to that exact target hostname.
4. Wait for propagation and re-check from a private window.
5. Confirm HTTPS certificate is issued and the browser shows a padlock.
6. Verify both URLs work:
   - free host URL (for example, yourname.netlify.app)
   - FlyRank subdomain (yourname.flyrank.ai)

This is why custom domain setup is a pointer change, not a rebuild. The website files and deployment process stay the same; DNS just tells the world which name should resolve to that existing site.
